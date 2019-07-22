
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class reparation(models.Model):
     _name = 'reparation.reparation'
     _description = ' '

     name= fields.Text(string="Identifiant",required=True)
     state = fields.Selection(string="Status", selection=[('en_cours', 'En cours'),('annule', 'Annulé'),
                                                          ('repare', 'Réparé'), ], default="en_cours", track_visibility='onchange', )
     biens=fields.Many2one(comodel_name="biens.biens",string="Bien à réparer", required=True)
     hab=fields.Many2one(comodel_name="habitants.habitants",string="Habitant")
     somme = fields.Float(string="Somme")
     datedebut= fields.Datetime(string="Date de début", default=fields.Datetime.now(), )
     datefin=fields.Datetime(string="Date de fin")
     info=fields.Text(string="Informations supplementaires")

     @api.constrains('datefin')
     def _check_datefin(self):
          if (self.datefin<self.datedebut):
               raise ValidationError("Date de fin invalide")

     @api.multi
     def en_cours_request(self):
          self.state = 'en_cours'

     @api.multi
     def annule_request(self):
          self.state = 'annule'

     @api.multi
     def repare_request(self):
          self.state = 'repare'