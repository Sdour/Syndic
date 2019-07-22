# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class calendrier(models.Model):
    _inherit = 'calendar.event'
    _description = ' '

    building_id = fields.Many2one('batiment.batiment', string='Bâtiment')
    attendee_string = fields.Char('Participants', compute='compute_participant')
    is_ag = fields.Char('AG')

    @api.one
    def compute_participant(self):
        self.attendee_string = ','.join(self.attendee_ids.mapped('name'))
