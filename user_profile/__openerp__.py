# -*- coding: utf-8 -*-
# © 2017 Oscar Ulises Garza Cordova
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "User Profile",
    "version": "9.0.1.0.0",
    "summary": "Basic Module to fill standard people data.",
    "author": "Oscar Ulises Garza Cordova",
    "license": "LGPL-3",
    "website": "",
    "category": "Generic Modules",
    "depends": ["base", "report"],
    "data": [
        "data/paper_format.xml",
        "security/ir.model.access.csv",
        "views/main_view.xml",
        "views/user_nickname_view.xml",
        "views/user_profile_view.xml",
        "report/user_profile_report.xml",
    ],
    'installable': True
}
