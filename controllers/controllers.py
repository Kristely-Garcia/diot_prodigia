# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/diotProdigia(http.Controller):
#     @http.route('/extra-addons/diot_prodigia/extra-addons/diot_prodigia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/diot_prodigia/extra-addons/diot_prodigia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/diot_prodigia.listing', {
#             'root': '/extra-addons/diot_prodigia/extra-addons/diot_prodigia',
#             'objects': http.request.env['extra-addons/diot_prodigia.extra-addons/diot_prodigia'].search([]),
#         })

#     @http.route('/extra-addons/diot_prodigia/extra-addons/diot_prodigia/objects/<model("extra-addons/diot_prodigia.extra-addons/diot_prodigia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/diot_prodigia.object', {
#             'object': obj
#         })