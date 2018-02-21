from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Category(models.Model):
    _name = "demo.category"

    name = fields.Char("Category Name")
    c_type = fields.Char("Category Type")

    @api.model
    def create(self, vals):
        print("------------------Model------------------------------------------")
        if self.search([('name', '=', vals.get('name'))]):
            raise ValidationError(_('Category already exists.'))
        return super(Category, self).create(vals)


class Product(models.Model):
    _name = "demo.product"

    name = fields.Char("Product Name")
    p_desc = fields.Text("Product Description")
    p_amount = fields.Integer("Product Amount")
    p_img = fields.Binary("Product Image")
    c_name = fields.Many2one("demo.category","Category Name")

    @api.constrains('p_amount')
    def _check_product_amount(self):
        print("------------------constrains------------------------------------------")
        if self.p_amount  < 500:
              raise ValidationError(_('Please enter an amount greater than 500'))

class Order(models.Model):
    _name = "demo.order"

    name = fields.Char("Order Name")
    note = fields.Text("Order Note")
    o_pro = fields.Many2many("demo.product",string="Product")

    @api.onchange('name')
    print("------------------onchange------------------------------------------")
    def _onchange_name(self):
        self.name = str(self.name) + "- Edited"