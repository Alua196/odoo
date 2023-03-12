from datetime import date
from odoo import api, fields, models


class TestTable1(models.Model):
    _name = "test.table1"
    _description = "Test Table 1"

    table2_id = fields.Many2one('test.table2', string='Table 2')
    field1 = fields.Char(string='Name', related='table2_id.field1')
    field3 = fields.Selection([('option1', 'Option1'), ('option2', 'Option2')], string='Option', related='table2_id.field3')
    # table2_m2o_num = fields.Many2one('test.table2', compute='_compute_age', string='Table 2')
    part_ids = fields.One2many('table1.part', 'table_id', string='Table 1 Parts')
    part_price = fields.Float(string='Part price', related='part_ids.price_unit')
    part_qty = fields.Integer(string='Part quantity', related='part_ids.qty')
    part_total = fields.Float(string='Total Price', compute='_compute_price')

    def _compute_price(self):
        for rec in self:
            if rec.part_qty:
                rec.part_total = rec.part_price * rec.part_qty
            else:
                rec.part_total = 0


class TestTable1Part(models.Model):
    _name = "table1.part"
    _description = "Test Table 1 Parts"

    part_id = fields.Many2one('product.product', required=True)
    qty = fields.Integer(string='Quantity')
    table_id = fields.Many2one('test.table1', string='Table')
    price_unit = fields.Float(related='part_id.list_price')