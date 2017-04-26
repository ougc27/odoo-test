# -*- coding: utf-8 -*-
# © 2017 Oscar Ulises Garza Cordova
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import api, fields, models


class UserProfile(models.Model):
    _name = "user.profile"

    name = fields.Char(
        required=True,)
    birthday = fields.Date(
        required=True,)
    gender = fields.Selection(
        [("m", "Male"),
         ("f", "Female")],
        required=True,)
    age = fields.Integer(
        compute="_compute_age",
        store=True,)
    hobbie_ids = fields.One2many(
        comodel_name="user.hobbie",
        inverse_name="user_id",
        string="Hobbies",)
    nickname_ids = fields.Many2many(
        "user.nickname",
        string="Nicknames",)
    notes = fields.Text()

    @api.depends("birthday")
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                date_now = fields.Date.from_string(fields.Date.today())
                difference = date_now - fields.Date.from_string(rec.birthday)
                rec.age = difference.days / 365