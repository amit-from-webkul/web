# -*- encoding: utf-8 -*-
############################################################################
#
#     Odoo, Open Source Web Widget IFrame
#     Authors: Laurent Mignon <laurent.mignon@acsone.eu>
#     Copyright (c) 2015 Acsone SA/NV (http://www.acsone.eu)
#
#     cmis_write_odoo_aspect is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     cmis_write_odoo_aspect is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with cmis_write_odoo_aspect.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Web Widget Color",
    'category': "web",
    'version': "1.0",
    "author": "ACSONE SA/NV, "
              "Odoo Community Association (OCA)",
    'depends': ['web'],
    'data': [
        'view/web_widget_iframe_view.xml'
    ],
    'qweb': [
        'static/src/xml/widget.xml',
    ],
    'auto_install': False,
    'installable': True,
    'web_preload': True,
}
