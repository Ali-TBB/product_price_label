# -*- coding: utf-8 -*-
{
    'name': 'Product Price Label',
    'summary': 'Product Price Label',
    'description': """
        Product Price label.
    """,
    'sequence': 1,
    'version': '1.0',
    'category': 'Productivity',
    'depends': [],
    'data': [
        #'security/ir.model.access.csv',
        'reports/product_price_label.xml',
        'views/product_price_label_template.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
