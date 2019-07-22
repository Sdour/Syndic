# -*- coding: utf-8 -*-

from odoo import models, fields, api

class appartement(models.Model):
     _name = 'appartement.appartement'
     _description = ' '
     #_sql_constraints = ['unique_app', 'unique(name,batiment)', 'Appartement déja exist!']

     name = fields.Char(string="Identifiant",required=True)
     batiment = fields.Many2one(comodel_name="batiment.batiment",string="Bâtiment", required=True)
     status = fields.Selection([('alloue', 'Alloué'), ('propriete', 'Propriété'), ('autre', 'Autre')], string='Status')
     info = fields.Text(string="informations suplémentaires")
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100