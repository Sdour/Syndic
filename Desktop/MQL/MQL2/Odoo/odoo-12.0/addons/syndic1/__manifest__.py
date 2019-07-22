# -*- coding: utf-8 -*-
{
    'name': "Syndic",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','calendar','purchase','muk_dms',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/appartement_view.xml',
        'views/batiment_view.xml',
        'views/habitants_view.xml',
        'views/biens_view.xml',
        'views/reunion_view.xml',
        'views/reparation_view.xml',
        'views/achat_view.xml',
        'views/document_view.xml',
        'views/calendrier_view.xml',
        'views/paiement_view.xml',
        'views/contributeur_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application':True,
    'installable':True,
}