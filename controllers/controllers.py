# -*- coding: utf-8 -*-
# from odoo import http


# class PatientMedicalRecord(http.Controller):
#     @http.route('/patient_medical_record/patient_medical_record', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/patient_medical_record/patient_medical_record/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('patient_medical_record.listing', {
#             'root': '/patient_medical_record/patient_medical_record',
#             'objects': http.request.env['patient_medical_record.patient_medical_record'].search([]),
#         })

#     @http.route('/patient_medical_record/patient_medical_record/objects/<model("patient_medical_record.patient_medical_record"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('patient_medical_record.object', {
#             'object': obj
#         })

