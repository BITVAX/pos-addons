# Copyright 2018 Dinar Gabbasov <https://it-projects.info/team/GabbasovDinar>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """POS: WeChat Mini-program""",
    "summary": """Integrate POS with WeChat mini-program""",
    "category": "Point of Sale",
    # "live_test_url": "",
    "images": ["images/pos_wechat_miniprogram.jpg"],
    "version": "11.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "apps@it-projects.info",
    "website": "https://github.com/itpp-labs/pos-addons#readme",
    "license": "Other OSI approved licence",  # MIT
    "depends": [
        "wechat_miniprogram",
        "pos_multi_session_restaurant",
        "pos_order_note",
        "pos_wechat",
        "base_geolocalize",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/ir.model.access.csv",
        "views/product_view.xml",
        "views/pos_wechat_miniprogram_view.xml",
        "views/template.xml",
        "views/pos_config_view.xml",
        "views/pos_restaurant_view.xml",
        "views/multi_session_view.xml",
        "wizard/qrcode.xml",
        "wizard/pos_payment_views.xml",
        "report/report_table_qrcode.xml",
    ],
    "demo": [],
    "qweb": [],
    "auto_install": False,
    "installable": True,
}
