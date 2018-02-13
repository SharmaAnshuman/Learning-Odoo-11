from odoo import models, fields

class Zapp(models.Model):
    _name = "z.app"
    id = fields.Integer("Note ID")
    name = fields.Char("Note Name")
    short_name = fields.Char('Note Short Title')
    lenght = fields.Float("Note Length")
    note = fields.Text("Note Text")
    issue = fields.Boolean("Note Issue")
    date = fields.Datetime("Note Date Time")
    cover = fields.Binary('Note Cover')
    state = fields.Selection([('draft', 'Not Available'),('available', 'Available'),('lost', 'Lost')],'State')
	
    