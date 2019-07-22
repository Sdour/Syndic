# -*- coding: utf-8 -*-

from odoo import models, fields, api

class biens(models.Model):
     _name = 'biens.biens'
     _description = ' '
     #_sql_constraints = ['unique_name','unique(name)','Identifiant déja exist!']

     name = fields.Char(string="Identifiant",copy=False, required=True)
     nom = fields.Char(string="Nom")
     nombre = fields.Integer(string="Nombre")
     batiment = fields.Many2one(comodel_name="batiment.batiment", string="Bâtiment", required=True)
     info = fields.Text(string="informations suplémentaires")
