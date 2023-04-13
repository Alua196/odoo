from datetime import date
from odoo import api, fields, models


class FurnitureProducts(models.Model):
    _name = "furniture.products"
    _description = "Furniture Products"

    name = fields.Char(string='Name')
    m_date = fields.Date(string='m_date')
    age = fields.Integer(string='Age', compute='_compute_age')
    cat_ids = fields.Many2many('furniture.categories', string='Categories')
    # cat = fields.Char(string='Category', related='cat_id.name')


    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.m_date:
                rec.age = today.year - rec.m_date.year
            else:
                rec.age = 0

