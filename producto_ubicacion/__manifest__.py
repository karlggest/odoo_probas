# -*- coding: utf-8 -*-
#############################################################################
#
#    TICPARAPYMES Carlos García Gestido
#
#    Copyright (C) 2020-TODAY Ticparapymes (<https://atendapc.net>).
#    Author: karlggest @ atendapc, (karl@atendapc.net)
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Etiqueta de Ubicación para Productos',
    'version': '15.0.1.0.0',
    'summary': 'Engade unha etiqueta para ordear a localización dos productos dentro do almacén',
    'category': 'stock',
    'author': 'karlggest',
    'company': 'atendapc',
    'website': 'https://github.com/karlggest/odoo_probas',
    'depends': ['stock',],
    'data': ['views/producto.xml',],
    'images': ['static/description/imaxe.jpg'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
