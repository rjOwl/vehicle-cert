from odoo import models, fields


class VvcCertificate(models.Model):
    _name = "vvc.certificate"
    _description = "Certificates Table"

    # serial_number = fields.Char(string='Serial', required=True)

    certificate_type_id = fields.Many2one("vvc.certificate.type")
    certificate_type = fields.Char(related="certificate_type_id.certificate_type")
    vehicle_type = fields.Selection([
        ("c", "Car"),
        ("b", "Bus"),
        ("mnb", "Minibus"),
        ("mcb", "Microbus")
    ])
    traffic_department = fields.Char()
    traffic_department_id = fields.Many2one("vvc.traffic.dept")
    traffic_department = fields.Char(related="traffic_department_id.department_name")

    customer = fields.Char()
    price = fields.Integer()
    motor_number = fields.Integer()
    chassis_number = fields.Char()
    car_model = fields.Char()
    brand = fields.Char()
