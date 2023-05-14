{
    'name' : 'Export Customer Pricelist Odoo',
    'author': "Edge Technologies",
    'version' : '14.0.1.2',
    'live_test_url':'https://youtu.be/R7oKfmikd2Q',
    "images":["static/description/main_screenshot.png"],
    'summary' : 'Apps help Customer Pricelist Export Pricelist Export Sales Pricelist Export Sale Pricelist Export Pricelist for Customer Price-List Export Price-List Export Sales Price-List Export Sale Price-List Export Customer Price List Export Price List for Customer',
    'description' : """
        Export Customer Pricelist
    """,
    "license" : "OPL-1",
    'depends' : ['base','sale_management'],
    'data': [
            'security/ir.model.access.csv',
            'data/export_customer_pricelist_temp.xml',
            'wizard/export_customer_pricelist.xml',
            'report/customer_pricelist_report.xml',
            'report/customer_report_template.xml',
            ],
    'qweb' : [],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'price': 22,
    'currency': "EUR",
    'category' : 'Sales',
}
