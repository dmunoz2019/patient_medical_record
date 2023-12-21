# -*- coding: utf-8 -*-
from odoo import models, fields

class ResDoctor(models.Model):
    _name = 'res.doctor'
    _description = 'Doctor'
    _inherits = {'res.partner': 'partner_id'}
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    
    patient_ids = fields.One2many('res.patient', 'doctor_id', string='Patients')
    channel_ids = fields.Many2many(
        "discuss.channel",
        "doctor_discuss_channel_member",  # New unique relation table name
        "doctor_id",  # Column for 'res.doctor'
        "channel_id",  # Column for 'discuss.channel'
        string="Channels",
        copy=False,)
    meeting_ids = fields.Many2many('calendar.event', 'calendar_event_res_doctor_rel', string='Meetings', copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
