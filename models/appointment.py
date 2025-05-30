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
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('cancelled', 'Cancelled'),
        ('done', 'Done')
    ], string='Status', default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == "New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)
  

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'
            record.message_post(body="Appointment confirmed.")
    def action_ongoing(self):
        for record in self:
            record.state = 'ongoing'
            record.message_post(body="Appointment is now ongoing.")
    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
            record.message_post(body="Appointment has been cancelled.")
    def action_done(self):
        for record in self:
            record.state = 'done'
            record.message_post(body="Appointment is now done.")
     