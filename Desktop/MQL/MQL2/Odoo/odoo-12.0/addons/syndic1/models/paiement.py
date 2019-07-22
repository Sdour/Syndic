# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta
from. import contributeur

class paiement(models.Model):
    _name = 'paiement.paiement'
    _description = ' '

    name = fields.Char(string="Facture",copy=False,required=True,default="Facture / "+str(fields.Datetime.now()),)
    hab = fields.Many2one(comodel_name="habitants.habitants",string="Habitant", required=True)
    date = fields.Datetime(string="Date de paiement", default=fields.Datetime.now(),)
    nbrmois = fields.Integer(string="Nombre de mois",default=1)
    du = fields.Datetime(string="Mois payé du")
    vers = fields.Datetime(string="Vers",readonly=True)
    somme = fields.Integer(string="Montant en DH",default=500)
    info = fields.Text(string="Informations")
    state = fields.Selection(string="Status", selection=[('in', 'in'), ('out', 'out'),], default="in")

    @api.constrains('nbrmois')
    def _check_nbrmois(self):
        if self.nbrmois <= 0:
            raise ValidationError("Nombre de mois non valide")

    def valider(self):
        self.vers = self.du + relativedelta(months=self.nbrmois)
        t = self.env['contributeur.contributeur'].search([('hab', '=', self.hab.id)]).nbr_paye
        t2 = self.env['contributeur.contributeur'].search([('hab', '=', self.hab.id)]).date
        t = t+self.nbrmois
        date_format = "%m/%d/%Y"
        a = datetime.strptime(str(t2.month)+"/"+str(t2.day)+"/"+str(t2.year), date_format)
        b = datetime.strptime(str(datetime.today().month)+"/"+str(datetime.today().day)+"/"+str(datetime.today().year), date_format)
        delta = b - a
        imp = int(delta.days/30 - t)
        if imp < 0 :
            imp = 0

        self._cr.execute("UPDATE public.contributeur_contributeur SET nbr_paye="+str(t)+", nbr_impaye="+str(imp)+" WHERE hab="+str(self.hab.id)+";")
        self.state='out'

    def envoyer(self):
        template_obj = self.env['mail.mail']
        template_data = {
            'subject': 'Facture',
            'body_html': 'Nom: '+ str(self.hab.name) +
                        '<br>Batiment: '+str(self.hab.app.batiment.name)
                        +'<br>Appartement: '+str(self.hab.app.name)
                        +'<br>Nombre de mois payé: '+str(self.nbrmois)
                        +'<br>Du: le '+str(self.du.month)+'-'+str(self.du.year)
                        +'<br>Vers: le '+str(self.vers.month)+'-'+str(self.du.year)
                        +'<br>Montant: '+str(self.somme)+'Dh'
                        +'<br>Date du paiement: '+str(self.date)+'<br>Syndic',
            'email_from': 'sdoureda@gmail.com',
            'email_to': str(self.hab.email)
        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)
        self.env['mail.mail'].process_email_queue()