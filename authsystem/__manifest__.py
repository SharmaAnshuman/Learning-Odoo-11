# -*- coding: utf-8 -*-
{
    'name': "Auth System",

    'summary': """
        My Auth System""",

    'description': """
        Desc
    """,

    'author': "Mohan Sharma",
    'website': "http://www.mohansharma.me",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/auth_view.xml'
    ],
}
