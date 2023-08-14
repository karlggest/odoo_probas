.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

Pendente de migración

==========================================
Contract Invoicing of Pending Sales Orders
==========================================

This modules is an particular adaptation from the OCA module. It brings OCA module the habiltity to include all pending to invoice sale orders without need of set the analytic account in each sale order. This way expands the OCA module to work with a large number of sale orders.

Usage
=====

To use this module, you need to:

#. Go to Invoicing > Sales > Contracts and select or create a new contract.
#. Check *Generate recurring invoices automatically*.
#. Mark the check "Invoice Pending Sales Orders".
#. Check *Factura por dirección de entrega" if you wish invoice only sale orders by delivery address.
#. On each invoicing, system will check the propper parent id and make the right invoices.


.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/110/11.0


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/contract/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors from OCA module
----------------------------

* `Tecnativa <https://www.tecnativa.com>`_:

  * Carlos Dauden

Do not contact contributors directly about support or help with technical issues.

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
