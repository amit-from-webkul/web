# -*- coding: utf-8 -*-
# Copyright 2014 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Help Online',
    'version': '9.0.1.0.0',
    'author': "ACSONE SA/NV,Odoo Community Association (OCA)",
    'maintainer': 'ACSONE SA/NV',
    'website': 'http://www.acsone.eu',
    'category': 'Documentation',
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'security/help_online_groups.xml',
        'security/help_online_rules.xml',
        'views/export_help_wizard_view.xml',
        'views/import_help_wizard_view.xml',
        'views/ir_ui_view_view.xml',
        'views/help_online_view.xml',
        'views/website_help_online.xml',
        'data/ir_config_parameter_data.xml',
    ],
    'qweb': [
        'static/src/xml/help_online.xml',
    ],
    'installable': True,
}
