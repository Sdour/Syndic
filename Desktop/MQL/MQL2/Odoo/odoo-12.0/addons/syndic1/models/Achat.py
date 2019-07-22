
from odoo import models, fields, api

class achat(models.Model):
     _name = 'achat.achat'
     _description = ' '
     _inherit = ["purchase.order"]