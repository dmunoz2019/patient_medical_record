# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HealthConsultation(models.Model):
    _name = 'health.consultation'
    _description = 'Health Consultation'
    _rec_name = 'name'

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Name must be unique"),
    ]
    name = fields.Char(string='Patient', readonly=True ,copy=True )
    
    
    @api.model
    def create(self, vals):
        if vals.get('name',  _('New')) ==  _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'health.consultation.sequence') or  _('New')
        result = super(HealthConsultation, self).create(vals)
        return result

    date = fields.Date(string='Consultation Date')
    weight = fields.Float(string='Weight')
    fat_percentage = fields.Float(string='Fat Percentage')
    water_percentage = fields.Float(string='Water Percentage')
    muscle_mass = fields.Float(string='Muscle Mass')
    physical_complexion = fields.Selection(
        [('1', 'Type 1'), ('2', 'Type 2'), ('3', 'Type 3')],
        string='Physical Complexion'
    )
    metabolic_age = fields.Integer(string='Metabolic Age')
    bone_density = fields.Float(string='Bone Density')
    visceral_fat = fields.Float(string='Visceral Fat')
    waist_circumference = fields.Float(string='Waist Circumference')
    abdomen_circumference = fields.Float(string='Abdomen Circumference')
    hip_circumference = fields.Float(string='Hip Circumference')
    bmi = fields.Float(string='BMI')
    pounds_lost = fields.Float(string='Pounds Lost')
    acupuncture = fields.Boolean(string='Acupuncture')
    fat_burn = fields.Boolean(string='Fat Burn')
    treatment_module = fields.Text(string='Treatment Module')
    patient_id = fields.Many2one('res.patient', string='Patient')
    doctor_id = fields.Many2one('res.doctor', string='Doctor')

