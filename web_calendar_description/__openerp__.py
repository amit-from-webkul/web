# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Web Calendar Description',
    'summary': """
        This module allows to add description into a calendar view
        depending of an ir.parameter""",
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NA,Odoo Community Association (OCA)',
    'website': 'https://acsone.eu',
    'depends': [
        'web_calendar',
    ],
    'data': [
        'views/web_calendar_description_view.xml',
    ],
}
