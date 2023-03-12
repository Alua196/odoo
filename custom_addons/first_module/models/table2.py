from datetime import date
from odoo import api, fields, models



class TestTable2(models.Model):
    _name = "test.table2"
    _description = "Test Table 2"

    field1 = fields.Char(string='name')
    fieldcomp = fields.Date(string='date')
    field2 = fields.Integer(string='number', compute='_compute_age')
    field3 = fields.Selection([('option1', 'option1'), ('option2', 'option2')], string='option')
    # date_comp_m2o = fields.Date(string='m2o date')
    tag_ids = fields.Many2many('test.table.tags', string='Tags')

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.fieldcomp:
                rec.field2 = today.year - rec.fieldcomp.year
            else:
                rec.field2 = 0
            # rec.field2 = date.today()
            # return rec.today.year - rec.fieldcomp.year    #- ((self.field2.month, self.field2.day) < (self.date.month, self.date.day))
