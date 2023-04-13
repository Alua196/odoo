{
    'name': 'Furniture Management',
    'version': '1.0.0',
    'category': '',
    'summary': 'Furniture Management',
    'description': """Furniture Management""",
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/products_view.xml',
        'views/categories_view.xml',
        'views/template.xml',
    ],
    'application': True,
    'sequence': -100,
    'auto_install': False,
    'license': 'LGPL-3',
}
