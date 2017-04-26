# -*- coding: utf-8 -*-
# © 2017 Oscar Ulises Garza Cordova
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class UserNickname(models.Model):
    _name = "user.nickname"

    name = fields.Char(
        required=True,)
