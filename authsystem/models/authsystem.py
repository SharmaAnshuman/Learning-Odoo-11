from odoo import models, fields

class AuthSystem(models.Model):
	_name = "authsystem"
	name = fields.Char("Name")