# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class batiment(models.Model):
     _name = 'batiment.batiment'
     _description = ' '
     #_sql_constraints = ['unique_batiment', 'unique(name)', 'Bâtiment déja exist!']

     name = fields.Char(string="Libellé",copy=False,required=True)
     nbrE = fields.Integer(string="Nombre des étages")
     nbrA = fields.Integer(string="Nombre des appartements")
     nbrAL = fields.Integer(string="Nombre des appartements libres")
     info = fields.Text(string="Informations")

     @api.constrains('nbrAL')
     def _check_nbrAL(self):
          if self.nbrAL > self.nbrA:
               raise ValidationError("Nombre des appartements vides non valide")

     @api.constrains('nbrE')
     def _check_nbrA(self):
          if self.nbrE > self.nbrA:
               raise ValidationError("Nombre des appartements non valide")