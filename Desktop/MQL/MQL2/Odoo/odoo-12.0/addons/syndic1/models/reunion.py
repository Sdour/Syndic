
from odoo import models, fields, api

class reunion(models.Model):
     _name = 'reunion.reunion'
     _description = ' '

     name = fields.Text(string="Objet",required=True)
     bat = fields.Many2one(comodel_name="batiment.batiment", string="Bâtiment")
     heure = fields.Date(string="Heure de début")
     lieu = fields.Text(string="Lieu")
     info = fields.Text(sting="info")

     def envoyer1(self):
          i = 0
          while i < 1000 :
               obj_product_product = self.env['habitants.habitants'].search([('id', '=', i)])
               print(obj_product_product.name)
               i += 1
               print(i)
               if obj_product_product.bat.id == self.bat.id :
                    template_obj = self.env['mail.mail']
                    template_data = {
                         'subject': 'Reunion : '+str(self.name),
                         'body_html': 'Nom: ' + str(obj_product_product.name) +
                                      '<br>Batiment: ' + str(self.bat.name)
                                      + '<br>Lieu: ' + str(self.lieu)
                                      + '<br>Date: ' + str(self.heure)
                                      + '<br>Cordialement.'
                                      + '<br>Syndic',
                         'email_from': 'sdoureda@gmail.com',
                         'email_to': str(obj_product_product.email)
                    }
                    template_id = template_obj.create(template_data)
                    template_obj.send(template_id)
          self.env['mail.mail'].process_email_queue()
          print('done1')

     def envoyer2(self):
          i = 0
          while i < 1000:
               obj_product_product = self.env['habitants.habitants'].search([('id', '=', i)])
               print(obj_product_product.name)
               i += 1
               if obj_product_product.name != False :
                    template_obj = self.env['mail.mail']
                    template_data = {
                         'subject': 'Reunion : '+str(self.name),
                         'body_html': 'Nom: ' + str(obj_product_product.name) +
                                      '<br>Batiment: ' + str(self.bat.name)
                                      + '<br>Lieu: ' + str(self.lieu)
                                      + '<br>Date: ' + str(self.heure)
                                      + '<br>Cordialement.'
                                      + '<br>Syndic',
                         'email_from': 'sdoureda@gmail.com',
                         'email_to': str(obj_product_product.email)
                    }
                    template_id = template_obj.create(template_data)
                    template_obj.send(template_id)
          self.env['mail.mail'].process_email_queue()
          print('done2')