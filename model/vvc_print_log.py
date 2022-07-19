from odoo import models, fields
import datetime


class PrintLog(models.Model):
    _name = 'print.log'

    certificate_id = fields.Many2one('vvc.certificate')
    user_id = fields.Many2one('res.users')
    date = fields.Date(default=datetime.today())
