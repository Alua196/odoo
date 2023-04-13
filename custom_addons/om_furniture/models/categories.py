from datetime import date
from odoo import api, fields, models



class FurnitureCategories(models.Model):
    _name = "furniture.categories"
    _description = "Furniture Categories"

    name = fields.Char(string='name', required=True)
    active = fields.Boolean(string='Active', default=True)
    # product_id = fields.Many2one('furniture.products', string='product')