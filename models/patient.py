from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Hospital Patient Master'

    name = fields.Char(string='Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='DOB', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    
