from odoo import models, fields


class VvcCustomer(models.Model):
    _name = "res.partner"
    _description = "Customers"

    customer_ids = fields.Many2one("vvc.certificate")

    # name = fields.Char()
    # Phone = fields.Char(related="vvc.")
