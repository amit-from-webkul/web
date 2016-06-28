# -*- coding: utf-8 -*-
# Copyright 2014 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os
import sys
import logging
import base64
from lxml import etree as ET

import openerp.tests.common as common
from openerp.tools.convert import convert_xml_import

_logger = logging.getLogger(__name__)


class TestExportHelpWizard(object):
    _data_files = ('data/help_test_data.xml',)

    _module_ns = 'help_online'

    def createPage(self, pageName, imgXmlId=False):
        imgId = False
        if imgXmlId:
            imgId = self.ref(imgXmlId)

        rootNode = ET.Element('t')
        rootNode.attrib['name'] = pageName
        rootNode.attrib['t-name'] = "website.%s" % pageName
        tNode = ET.SubElement(rootNode,
                              't',
                              attrib={'t-call': 'website.layout'})
        structDivNode = ET.SubElement(tNode,
                                      'div',
                                      attrib={'class': 'oe_structure oe_empty',
                                              'id': 'wrap'})
        sectionNode = ET.SubElement(structDivNode,
                                    'section',
                                    attrib={'class': 'mt16 mb16'})
        containerNode = ET.SubElement(sectionNode,
                                      'div',
                                      attrib={'class': 'container'})
        rowNode = ET.SubElement(containerNode,
                                'div',
                                attrib={'class': 'row'})
        bodyDivNode = ET.SubElement(rowNode,
                                    'div',
                                    attrib={'class': 'col-md-12 '
                                                     'text-center mt16 mb32'})
        style = "font-family: 'Helvetica Neue', Helvetica,"\
                " Arial, sans-serif; color: rgb(51, 51, 51);"\
                " text-align: left;"
        h2Node = ET.SubElement(bodyDivNode,
                               'h2',
                               attrib={'style': style})
        h2Node.text = "Test Sample Title"
        if imgId:
            imgDivNode = ET.SubElement(bodyDivNode,
                                       'div',
                                       attrib={'style': 'text-align: left;'})
            src = "/website/image?field=datas&"\
                  "model=ir.attachment&id=%s" % str(imgId)
            ET.SubElement(imgDivNode,
                          'img',
                          attrib={'class': 'img-thumbnail',
                                  'src': src})
            imgDivNode = ET.SubElement(bodyDivNode,
                                       'div',
                                       attrib={'style': 'text-align: left;'})
            src = "/website/image/ir.attachment/%s_ccc838d/datas" % str(imgId)
            ET.SubElement(imgDivNode,
                          'img',
                          attrib={'class': 'img-thumbnail',
                                  'src': src})
        arch = ET.tostring(rootNode, encoding='utf-8', xml_declaration=False)
        vals = {
            'name': pageName,
            'type': 'qweb',
            'arch': arch,
            'page': True,
        }
        view_id = self.env['ir.ui.view'].create(vals)
        return view_id.id

    def setUp(self):
        super(TestExportHelpWizard, self).setUp()
        self.pageName = False
        self.imgXmlId = False
        self.pageTemplate = False
        # Loads the data file before
        module = sys.modules[self.__class__.__module__]
        base_path = os.path.dirname(module.__file__)
        for path in self._data_files:
            path = path.split('/')
            path.insert(0, base_path)
            path = os.path.join(*path)
            convert_xml_import(self.cr, self._module_ns, path)

    def test_export_help(self):
        """
            Export help data
        """
        self.createPage(pageName=self.pageName, imgXmlId=self.imgXmlId)

        wizardPool = self.env['export.help.wizard']
        wizard = wizardPool.create({})
        wizard.export_help()
        xmlData = base64.decodestring(wizard.data)

        parser = ET.XMLParser(remove_blank_text=True)
        rootXml = ET.XML(xmlData, parser=parser)

        xPath = ".//template[@id='website.%s']" % self.pageName
        templateNodeList = rootXml.findall(xPath)
        self.assertEqual(len(templateNodeList), 1)
        self.assertNotIn("website.", templateNodeList[0].attrib['name'])

        if self.imgXmlId:
            xPath = ".//record[@id='%s']" % self.imgXmlId
            imgNodeList = rootXml.findall(xPath)
            self.assertEqual(len(imgNodeList), 1,
                             'The same image should be exported only once')

            for imgElem in templateNodeList[0].iter('img'):
                imgSrc = imgElem.get('src')
                if '/ir.attachment/' in imgSrc:
                    self.assertIn("/ir.attachment/%s|"
                                  % self.imgXmlId, imgSrc)
                else:
                    self.assertIn("/web/image/%s" % self.imgXmlId, imgSrc)

        if self.pageTemplate:
            xPath = ".//template[@id='website.%s_snippet']" % self.pageName
            templateNodeList = rootXml.findall(xPath)
            self.assertEqual(len(templateNodeList), 1)
            self.assertNotIn("website.", templateNodeList[0].attrib['name'])


class TestExportHelpWithImage(TestExportHelpWizard, common.TransactionCase):
    def setUp(self):
        super(TestExportHelpWithImage, self).setUp()
        parameter_model = self.env['ir.config_parameter']
        page_prefix = parameter_model.get_param('help_online_page_prefix')
        self.pageName = '%stest-page' % page_prefix
        self.imgXmlId = '%s.test_img_1' % self._module_ns


class TestExportHelpTemplate(TestExportHelpWizard, common.TransactionCase):
    def setUp(self):
        super(TestExportHelpTemplate, self).setUp()
        parameter_model = self.env['ir.config_parameter']
        param = 'help_online_template_prefix'
        template_prefix = parameter_model.get_param(param)
        self.pageName = '%stest-template' % template_prefix
        self.pageTemplate = True
