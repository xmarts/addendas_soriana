# -*- coding: utf-8 -*-
from odoo import models, fields, api


import logging

_logger = logging.getLogger(__name__)
class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_values_addenda(self):
        print('---------------------------_get_values_addenda-----------------------------')
        for rec in self:
            for l in rec.edi_document_ids:
                cfdi_3_3_edi = self.env.ref('l10n_mx_edi.edi_cfdi_3_3')
                if l.edi_format_id == cfdi_3_3_edi:
                    invoice = l.move_id
                    xml = l.edi_format_id._l10n_mx_edi_get_invoice_cfdi_values(invoice)
                    _logger.warning(xml)
                    return xml