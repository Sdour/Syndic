# -*- coding: utf-8 -*-
from odoo import http

# class Syndic1(http.Controller):
#     @http.route('/syndic1/syndic1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syndic1/syndic1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syndic1.listing', {
#             'root': '/syndic1/syndic1',
#             'objects': http.request.env['syndic1.syndic1'].search([]),
#         })

#     @http.route('/syndic1/syndic1/objects/<model("syndic1.syndic1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syndic1.object', {
#             'object': obj
#         })