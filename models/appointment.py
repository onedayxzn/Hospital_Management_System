from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment Master'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True, tracking=True)
    note = fields.Text(string='Note', tracking=True)
    reference = fields.Char(string='Reference', required=True, tracking=True, default="New")

    @api.model_create_multi
    def create(self, vals_list):
        print("Creating appointment with vals_list:", vals_list)    
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == "New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        print("Creating appointment with vals_list after modification:", vals_list)

        return super().create(vals_list)
  