# -*- coding: utf-8 -*-
{
    'name': "Patient medical record",

    'summary': "Keep track of patient's medical record",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Medical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'calendar', 'sale', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/health_consultation.xml',
        'views/res_patient.xml',
        'views/res_doctor.xml',
        'data/ir_sequence_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

