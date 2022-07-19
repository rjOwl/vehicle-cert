from odoo import models, fields


class VvcTrafficDepartment(models.Model):
    _name = "vvc.traffic.dept"
    _description = "Traffic Department"

    name = fields.Char()
    # patient_ids = fields.One2many("hms.patient", "department_id")
