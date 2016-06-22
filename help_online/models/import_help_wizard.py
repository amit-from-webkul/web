# -*- coding: utf-8 -*-
# Copyright 2014 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
from openerp.tools import convert

import base64
from cStringIO import StringIO


class ImportHelpWizard(models.TransientModel):
    _name = "import.help.wizard"

    source_file = fields.Binary('Source File')

    @api.one
    def import_help(self):
        source_file = base64.decodestring(self.source_file)
        convert.convert_xml_import(self.env.cr,
                                   self._module,
                                   StringIO(source_file),
                                   idref=None,
                                   mode='init',
                                   noupdate=False,
                                   report=None)
