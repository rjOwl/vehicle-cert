from odoo import models, fields


class VvcCertificateType(models.Model):
    _name = "vvc.certificate.type"
    _description = "Certificate Types Table"
    _rec_name = "type"

    type = fields.Char()
