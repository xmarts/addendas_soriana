# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AddRateAddressDelivery(models.Model):
	_inherit = 'res.partner'

	rate_address = fields.Many2one( 'product.pricelist', string = 'Tarifa' )
	most_ieps = fields.Boolean( string = 'Mostrar IEPS' )
	number_sucursal = fields.Char( string="Numero" )
	type_suc = fields.Selection( [('A','Cedis'),('S','Sucursal'),('O','Oficinas')] , string = 'Tipo')
	type_customer = fields.Selection([('mayorista','Mayorista'),('maquila','Maquila'),('autoservicios','Autoservicios'),('rutas','Rutas')], string = 'Tipo de cliente')
	format_suc = fields.Char( compute = "getValue", readonly=True )
	gln = fields.Char( string = 'GLN' )
	number_provideer = fields.Char( string = 'Numero de proveedor' )
	shipping_number_provider = fields.Char( string = "Numero de proveedor" )
	shipping_number_store = fields.Char( string = "Numero de tienda" )
	shipping_number_cedis = fields.Char( string = "Numero de cedis" )
	shipping_type_suc = fields.Selection( [('A','Cedis'),('S','Sucursal'),('O','Oficinas')] , string = 'Tipo')
	shipping_gln = fields.Char( string = "GLN" )
	contact_name = fields.Char(string="Nombre de contacto")

	def getValue(self):
		if self.number_sucursal and self.type_suc:
			self.format_suc = str(self.type_suc) + str(self.number_sucursal)
		else:
			self.format_suc = ''

class AddFieldsContacts(models.Model):
	_inherit = 'res.partner'
	number_store = fields.Char( string = "Numero de tienda" )

class AddFieldsBank(models.Model):
	_inherit = "res.partner.bank"

	last_acc_number = fields.Char(string="ultimos 4 digitos")

	def get_last_numbers(self):
		if self.acc_number:
			self.last_acc_number = self.acc_number[-4:]