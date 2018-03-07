import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Clients(models.Model):
    _name = "pma.clients"

    name = fields.Char("Client Name", size=30, required=True)
    website = fields.Char("Website", size=60, default="http://www.")
    industry = fields.Char("Industry", required=True)
    revenue = fields.Integer("Revenue", default=29000)
    description = fields.Text("Description")
    phone = fields.Char("Phone", size=10, required=True)
    street1 = fields.Text("Street1")
    street2 = fields.Text("Street2")
    city = fields.Char("City")
    state = fields.Char("State")
    zipcode = fields.Integer("Zip Code")
    country = fields.Char("Country")
    note = fields.Text("Note")

    @api.constrains('phone')
    def _check_phone(self):
        pattern = "^[0-9]{10}$"
        if not re.match(pattern, self.phone):
            raise ValidationError(_('Please Enter 10 Digit Phone Number'))


class Contacts(models.Model):
    _name = "pma.contacts"

    name = fields.Char("Contact Name", size=30, required=True)
    title = fields.Char("Title", size=30, required=True)
    fname = fields.Char("First Name", size=30, required=True)
    mname = fields.Char("Middle Name", size=30, required=True)
    lname = fields.Char("Last Name", size=30, required=True)
    email = fields.Char("Email", required=True)
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')], "Gender", required=True)
    occupation = fields.Char("Occupation", required=True)
    phone = fields.Char("Phone", size=10, required=True)
    dob = fields.Datetime("Birth Of Day")
    note = fields.Text("Note")
    client_contact = fields.Many2one("pma.clients", "Client")

    @api.constrains('phone')
    def _check_phone(self):
        pattern = "^[0-9]{10}$"
        if not re.match(pattern, self.phone):
            raise ValidationError(_('Please Enter 10 Digit Phone Number'))


class Milestone(models.Model):
    _name = "pma.milestones"

    name = fields.Char("Milestone")
    duedate = fields.Datetime("Due Date")
    deliverables = fields.Text("Deliverables")
    status = fields.Char("Status")
    project_ids = fields.Many2one("pma.projects", "Project")
    total_hours = fields.Float("Total Hours")


class Task(models.Model):
    _name = "pma.tasks"
    project_ids = fields.Many2one("pma.projects","Project")
    emp_ids = fields.Many2one("res.users","Employee",domain=lambda self: [("groups_id", "=", self.env.ref( "pma.group_employee" ).id)])
    name = fields.Char("Task Name")
    instrucation = fields.Char("Instrucation")
    total_hours = fields.Float("Total Hours")
    status = fields.Text("Task Status")


class Costs(models.Model):
    _name = "pma.employee"

    name = fields.Char("Name")
    description = fields.Char("Description")
    priceper = fields.Float("Price Per")
    quantity = fields.Integer("Quantity")
    total_cost = fields.Float("Total Cost")
    project_ids = fields.Many2one("pma.projects", "Project")
    milestones_ids = fields.Many2one("pma.milestones", "Milestone")


class Projects(models.Model):
    _name = "pma.projects"

    name = fields.Char("Project Name")
    start_date = fields.Datetime("Start Date")
    hourly_rate = fields.Float("Hourly Rate")
    budget = fields.Integer("Budget")
    active_state = fields.Char("Active")
    total_hours = fields.Float("Total Hours")
    labor_cost = fields.Float("Labor Cost")
    material_cost = fields.Float("Material Cost")
    total_cost = fields.Float("Total Cost", compute="_generate_total_cost", store=True)
    manager_id = fields.Many2one("res.users","Project Manager",domain=lambda self: [("groups_id", "=", self.env.ref( "pma.group_manager" ).id)])
    status = fields.Char("Project Status")
    state = fields.Selection(
        [('draft', 'Draft'), ('register', 'Registered'), ('confirm', 'Confirmed'), ('cancel', 'Cancelled'), ],
        string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    client = fields.Many2one("pma.clients", "Client")

    @api.depends('hourly_rate', 'total_hours', 'material_cost', 'labor_cost', 'total_cost')
    def _generate_total_cost(self):
        print("------------------Depends------------------------------------------")
        for record in self:
            tmp = (record.hourly_rate * record.total_hours) + (record.labor_cost + record.material_cost)
            record.total_cost = tmp
