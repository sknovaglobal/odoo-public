
{
    'name': 'Hide Pages (tabs) for Users',
    'version': '1.0.0',
    'summary': 'Configure form page visibility for selected Odoo users',
    'description': """
Hide Pages for Users
====================

Configure the visibility of selected notebook pages (tabs) in Odoo forms
for specific users.

Features:
- Configure page restrictions from the Odoo backend.
- Assign restrictions to selected users.
- Keep the interface focused for different user roles.
- Apply configured page visibility using a backend JavaScript asset.

Security note:
Hiding a page in the user interface does not replace Odoo access rights,
record rules, or server-side security controls.
    """,
    'category': 'Productivity',
    'author': 'SkNovaGlobal',
    'website': 'https://sknovaglobal.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/page_restriction_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hide_page_user/static/src/js/page_restriction.js',
        ],
    },
    'images': [
            'static/description/project_overview.png',
            'static/description/banner.png',
            'static/description/icon.png',
        ],
    'installable': True,
    'application': False,
}
