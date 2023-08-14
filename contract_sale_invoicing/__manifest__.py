# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Contract Invoicing of Pending Sales Orders',
    'summary': 'Include sales to invoice in contract invoice creation',
    'version': '15.0.2.0.0',
    'category': 'Contract Management',
    'website': 'https://github.com/oca/contract',
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
              'karlggest'
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'contract',
        'sale_management',
    ],
    'data': [
        'views/contract_view.xml',
    ],
}
