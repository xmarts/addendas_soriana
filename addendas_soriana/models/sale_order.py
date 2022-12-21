# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class OnchangeDirectionFacture(models.Model):

	_inherit = 'sale.order'

	addenda_normal = fields.Boolean( string = "Factura normal" , default = False )
	addenda_extemporanea = fields.Boolean( string = "Factura extemporanea" , default = False)
	number_order = fields.Char( string = "Numero de orden" )
	number_appoi = fields.Char( string = "Numero de cita" )
	date_of_order = fields.Date( string = "Fecha del pedido del cliente" )
	date_of_deli = fields.Date( string = "Fecha de entrega")
	folio_note_entry = fields.Char( string = "Folio de nota de entrada" )
	field_add_capture = fields.Char( string = "Campo addicional para capturar" )

	@api.onchange('addenda_normal')
	def changeAddendaNormal(self):
		if self.addenda_normal == True:
			self.addenda_extemporanea = False
			search = self.env['ir.ui.view'].search([('name','=','SorianaFacturaNormal')], limit = 1)
			if search:
				self.partner_id.write({'l10n_mx_edi_addenda':search.id})

	@api.onchange('addenda_extemporanea')
	def changeAddendaExtemporanea(self):
		if self.addenda_extemporanea == True:
			self.addenda_normal = False
			search = self.env['ir.ui.view'].search([('name','=','SorianaFacturaExtemporanea')], limit = 1)
			if search:
				self.partner_id.write({'l10n_mx_edi_addenda':search.id})

	@api.onchange('partner_shipping_id')
	def changeDirFac(self):
		if self.partner_shipping_id:
			if self.partner_shipping_id.rate_address.id:
				self.pricelist_id = self.partner_shipping_id.rate_address.id
			else:
				self.pricelist_id = self.partner_shipping_id.property_product_pricelist.id