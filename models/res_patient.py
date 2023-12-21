# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPatient(models.Model):
    _name = 'res.patient'
    _description = 'Patient'
    _inherits = {'res.partner': 'partner_id'}


    name = fields.Char(string='Name', required=True)
    blood_type = fields.Selection([
        ('a+', 'A+'), 
        ('a-', 'A-'),
        ('b+', 'B+'), 
        ('b-', 'B-'),
        ('ab+', 'AB+'), 
        ('ab-', 'AB-'),
        ('o+', 'O+'), 
        ('o-', 'O-')
    ], string='Blood Type')
    doctor_id = fields.Many2one('res.doctor', string='Doctor')
    channel_ids = fields.Many2many(
    "discuss.channel",
    "patient_discuss_channel_member",  # New unique relation table name
    "res_patient_id",  # Column for 'res.patient'
    "channel_id",  # Column for 'discuss.channel'
    string="Channels",
    copy=False,)
    meeting_ids = fields.Many2many('calendar.event', 'calendar_event_res_patient_rel', 'patient_id',
                                   'calendar_event_id', string='Meetings', copy=False)
    consultations_ids = fields.One2many(
        comodel_name='health.consultation',  # Replace with your consultation model's name
        inverse_name='patient_id',           # Field in 'health.consultation' that refers to 'res.patient'
        string='Consultations'
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    