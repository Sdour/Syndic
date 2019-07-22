# -*- coding: utf-8 -*-
from ntsecuritycon import DS_UNIQUE_ID_NAME

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class habitants(models.Model):
     _name = 'habitants.habitants'
     _description = ' '
     #_inherit = ["res.partner"]

     photo =fields.Binary(string="Photo")
     name = fields.Text(string="Nom", required=True)
     prenom =fields.Text(string="Prenom")
     tel = fields.Text(string="Telephone")
     email = fields.Text(string="Email", required=True)
     info = fields.Text(string="Informations supplementaires")
     status = fields.Selection([('l', 'Locataire'), ('p', 'Propriétaire'), ('autre', 'Autre')], string='Status')
     app = fields.Many2one(comodel_name="appartement.appartement", string="Appartement", required=True)
     bat = fields.Many2one(comodel_name="batiment.batiment", string="Bâtiment", readonly=True)
     state = fields.Selection(string="Status", selection=[('in', 'in'), ('out', 'out'), ], default="in")

     @api.constrains('email')
     def _check_email(self):
          if not self.email.endswith('@gmail.com'):
               raise ValidationError("Email non valide")

     def validerhab(self):
          self._cr.execute(
               "INSERT INTO public.contributeur_contributeur(hab, date, nbr_paye, nbr_impaye, app,bat) VALUES (" + str(
                    self.id) +", current_date ," + str(0) + "," + str(0) + ","+ str(self.app.id) +","+ str(self.app.batiment.id) +");")
          self.state='out'
          self.bat = self.app.batiment

     @api.onchange('app')
     def _onchange_app(self):
          self.bat = self.app.batiment