# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2010-2012 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>). 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Italian Localisation - Account',
    'version': '0.2',
    'category': 'Localisation/Italy',
    'description': """This module customizes OpenERP in order to fit italian laws and mores - Account version

Functionalities:

- Fiscal code computation for partner
- Check invoice date consistency

""",
    'author': "OpenERP Italian Community,Odoo Community Association (OCA)",
    'website': 'http://www.openerp-italia.org',
    'license': 'AGPL-3',
    "depends" : ['account','base_vat','account_chart','base_iban', 'l10n_it_base','account_invoice_entry_date'],
    "init_xml": [
        'account/partner_view.xml',
        'account/invoice_view.xml',
        'wizard/fiscalcode_to_data_view.xml',
    ],
    "update_xml" : [],
    "demo_xml" : [],
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

