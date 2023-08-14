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
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import models, fields, api

class ProductUbicacion(models.Model):
    _inherit = 'product.template'

    etiqueta_ubicacion = fields.Char('Etiqueta de Ubicacion');


