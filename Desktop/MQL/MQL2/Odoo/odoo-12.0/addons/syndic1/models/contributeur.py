# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class contributeur(models.Model):
    _name = 'contributeur.contributeur'
    _description = ' '

    hab = fields.Many2one(comodel_name="habitants.habitants",string="Habitant", required=True,readonly="true")
    app = fields.Many2one(comodel_name="appartement.appartement",string="Appartement", required=True,readonly="true")
    bat = fields.Many2one(comodel_name="batiment.batiment",string="Bâtiment", required=True,readonly="true")
    date = fields.Datetime(string="Date de début",readonly="true")
    nbr_paye = fields.Integer(string="Nombre de mois payé",readonly="true")
    nbr_impaye = fields.Integer(string="Nombre de mois impayé",readonly="true")
    info = fields.Text(string="Informations")

    def init(self):
        print("SELECT hab FROM public.contributeur_contributeur;")
        i = 0
        t=0
        while i < 1000 :
            obj_product_product = self.env['contributeur.contributeur'].search([('hab', '=',i)])
            if obj_product_product.id != False :
                print(obj_product_product.id)
                t2 = obj_product_product.date
                t = obj_product_product.nbr_paye
                date_format = "%m/%d/%Y"
                a = datetime.strptime(str(t2.month) + "/" + str(t2.day) + "/" + str(t2.year), date_format)
                b = datetime.strptime(
                    str(datetime.today().month) + "/" + str(datetime.today().day) + "/" + str(datetime.today().year),
                    date_format)
                delta = b - a
                print(delta.days / 30)
                imp = int(delta.days / 30 - t)
                print(imp)
                if imp < 0:
                    imp = 0
                t=imp
                self._cr.execute("UPDATE public.contributeur_contributeur SET nbr_impaye=" + str(imp) + " WHERE hab=" + str(i) + ";")
            if t > 0 and int(datetime.today().day) == 1 :
                template_data = {
                    'subject': 'Avis de contribution',
                    'body_html': 'Bonjour '+ str(obj_product_product.hab.name) + ',<br>Merci de bien '
                                'vouloir payer la contribution mensuelle convenu.<br>Nombre '
                                'de mois non payé: '+str(t)+'.<br>Cordialement.<br>Syndic.',
                    'email_from': 'sdoureda@gmail.com',
                    'email_to': str(obj_product_product.hab.email)
                }
                template_obj = self.env['mail.mail']
                template_id = template_obj.create(template_data)
                template_obj.send(template_id)

            i+=1
        self.env['mail.mail'].process_email_queue()