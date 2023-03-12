from odoo import api, fields, models


class TestTable1(models.Model):
    _name = "test.table1"
    _description = "Test Table 1"

    table2_id = fields.Many2one('test.table2', string='Table 2')

    # field1 = fields.Char(string='field1')
    # field2 = fields.Integer(string='field2')
    # field3 = fields.Selection([('option1', 'option1'), ('option2', 'option2')], string='field3')