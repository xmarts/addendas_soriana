# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):

	_inherit = 'account.move'
	
	commitment_date  = fields.Date(string='Fecha de entrega de mercancia')
	number_cita = fields.Char(string='Cita')
	entry_note_folio = fields.Char(string='Folio nota de entrada')
	folio_pedido = fields.Char(string='Folio pedido')


