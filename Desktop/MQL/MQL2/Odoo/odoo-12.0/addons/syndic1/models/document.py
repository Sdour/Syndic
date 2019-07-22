
from odoo import models, fields, api

class document(models.Model):
     _name = 'document.document'
     _description = ' '
     _inherit = ["muk_dms.file"]