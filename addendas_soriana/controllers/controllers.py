# -*- coding: utf-8 -*-
from odoo import http

# class AddendasSoriana(http.Controller):
#     @http.route('/addendas_soriana/addendas_soriana/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addendas_soriana/addendas_soriana/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addendas_soriana.listing', {
#             'root': '/addendas_soriana/addendas_soriana',
#             'objects': http.request.env['addendas_soriana.addendas_soriana'].search([]),
#         })

#     @http.route('/addendas_soriana/addendas_soriana/objects/<model("addendas_soriana.addendas_soriana"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addendas_soriana.object', {
#             'object': obj
#         })