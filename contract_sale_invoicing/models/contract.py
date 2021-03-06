# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    invoicing_sales = fields.Boolean(
        string='Invoice Pending Sales Orders',
        help='If checked include sales with same analytic account to invoice '
             'in contract invoice creation.',
    )
    invoicing_by_delivery = fields.Boolean(
            string='Factura Por Dirección de Entrega',
            help='De marcarse, as facturas faranse só para a dirección de entrega '
            'seleccionada no campo cliente (partner_id)',
            )

    @api.multi
    def _create_invoice(self, invoice=False):
        if not self.invoicing_sales:
            return super(AccountAnalyticAccount, self)._create_invoice()
        if self.invoicing_by_delivery:
            sales = self.env['sale.order'].search([
                ('partner_id', '=', self.partner_id.id),
                ('invoice_status', '=', 'to invoice'),
                ('date_order', '<=',
                 '{} 23:59:59'.format(self.recurring_next_date)),
            ])
        else:
            sales = self.env['sale.order'].search([
                ('partner_invoice_id', 'child_of',
                 self.partner_id.commercial_partner_id.ids),
                ('invoice_status', '=', 'to invoice'),
                ('date_order', '<=',
                 '{} 23:59:59'.format(self.recurring_next_date)),
            ])
        if sales:
            invoice_ids = sales.action_invoice_create()
            invoice = self.env['account.invoice'].browse(invoice_ids)[:1]
        return super(AccountAnalyticAccount, self)._create_invoice(
            invoice=invoice)
