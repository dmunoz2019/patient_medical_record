# -*- coding: utf-8 -*-
from odoo import models, fields , api, _

class ResDoctor(models.Model):
    _name = 'res.doctor'
    _description = 'Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}
    _rec_name = 'name'
    doctor_id = fields.Char(string='Doctor ID', required=True, copy=False, readonly=True, index=True, store=True)

    doctor_name = fields.Char(string='Doctor Name', required=True , related='partner_id.name', store=True, readonly=False)
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
    def _get_mail_thread_data(self, request_list):
        res = super(ResDoctor, self)._get_mail_thread_data(request_list)
        return res