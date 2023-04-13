from datetime import date
from odoo import api, fields, models



class TestTableTags(models.Model):
    _name = "test.table.tags"
    _description = "Test Table Tags"

    name = fields.Char(string='name', required=True)
    active = fields.Boolean(string='Active', default=True)