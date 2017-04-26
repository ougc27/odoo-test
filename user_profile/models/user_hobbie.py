# -*- coding: utf-8 -*-
# © 2017 Oscar Ulises Garza Cordova
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models


class UserHobbie(models.Model):
    _name = "user.hobbie"

    name = fields.Char(
        required=True,)
    dedicated_hours = fields.Float(
        required=True,)
    user_id = fields.Many2one(
        comodel_name="user.profile",
        string="User",)
