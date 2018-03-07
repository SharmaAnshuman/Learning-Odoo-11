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
    p_sale_amount = fields.Integer("Product Sale Price",compute="_adding_fee_amount",store=True)

    @api.depends('p_amount','p_sale_amount')
    def _adding_fee_amount(self):
        print("------------------Depends------------------------------------------")
        for record in self:
            record.p_sale_amount = record.p_amount + 150

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
    def _onchange_name(self):
        print("------------------onchange------------------------------------------")
        self.name = str(self.name) + "- Edited"
