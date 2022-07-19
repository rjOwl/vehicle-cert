from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date

# https://www.odoo.com/forum/help-1/validation-error-nameerror-name-is-not-defined-170768
# https://www.odoo.com/forum/help-1/what-is-sequence-id-in-odoo10-137508


class VvcCertificate(models.Model):
    _name = "vvc.certificate"
    _description = "Certificates Table"

    serial_number = fields.Char()
    curr_date = date.today()
    certificate_type_id = fields.Many2one("vvc.certificate.type")
    # certificate_type = fields.Char(related="certificate_type_id.certificate_type")
    vehicle_type = fields.Selection([
        ("c", "Car"),
        ("b", "Bus"),
        ("mnb", "Minibus"),
        ("mcb", "Microbus")
    ])
    traffic_department_id = fields.Many2one("vvc.traffic.dept")
    # traffic_department = fields.Char(related="traffic_department_id.department_name")

    # customer = fields.Char()
    customer_ids = fields.Many2one('res.partner', 'Customer')
    price = fields.Integer()
    motor_number = fields.Char()
    chassis_number = fields.Char()
    car_model = fields.Selection(selection=[
        (str(date.today().year - i), str(date.today().year - i))
        for i in range(21)])
    brand = fields.Many2one("vvc.brands")

    @api.model
    def create(self, vals):
        if vals.get('serial_number', _('New')) == _('New'):
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('seq_serial_number') or _('New')
        res = super(VvcCertificate, self).create(vals)
        return res

    @api.onchange('motor_number')
    def _onchange_check_motor_number(self):
        if not str(self.motor_number).isdigit():
            return {'domain': {},
                    'warning': {'title': 'Motor Number',
                                'message': "Only digits allowed"}}

    # @api.onchange('car_model')
    # def _onchange_set_car_model(self):
    #     print("Selected model:", self.car_model)
    #     current_year = date.today().year
    #     valid_years =[(str(current_year - i), str(current_year - i))
    #             for i in range(5)])
    #     # self.car_model = valid_years
    #
    #     return {'domain': {'car_model': valid_years},
    #             'warning': {'title': 'message', 'message': "test"}}

    def print_certificate(self):
        print("Printed")
        return self.env.ref('vvc.vvc_certificate_report_action').report_action(self)


class Brands(models.Model):
    _name = "vvc.brands"
    name = fields.Char()


class ReportTemplate:
    @staticmethod
    def use_lang(lang="ar"):
        language_dic = {
            "ar": {
                "name": "السدد اللواء مدير ادارة مرور",
                "date ": "تحرير في",
                "greetings": "تحية طيبة وبعد ،،،،",
                "certificate_type": "أشرف بافادة سيادتكم بأنه تم تعديل",
                "chassis": "شاسية رقم",
                "motor": "محرك رقم",
                "brand": "الماركة",
                "model": "الموديل",
                "customer": "اسم المالك",
                "body": "ها حيث أن المؤسسة معتمدة بالهيئة العامة للتنمية الصناعية ومصلحة الرقابة الصناعية ومعتمدة بادارات المرور ولها سجل تجاري صناعي وبطاقة ضريبية بهذه الصفة وقد تم فحص التعديل والتركيب واللحامات والإصلاحات اللازمة طبقا لأصول الصناعة ودون الإخلال بالتصميم الأصلي ودون المساس بالأجزاء الجوهرية للسيارة وقد تم تجربة السيارة على الطرق المصرية ووجد أنها متزنة وهذه شهادة منا بتلك لتقديمها المرور والمالك مسؤول مسئولية كاملة عن بيانات الشهادة فبرجاء التكرم والتفضل بالموافقة على ترخيص السيارة",
                "ending": "وتفضلوا بقبول فائق الاحترام والتقدير،،،،",
            },
            "en": {
                "name": "Traffic Department",
                "date ": "Date",
                "greetings": "تحية طيبة وبعد ،،،،",
                "certificate_type": "أشرف بافادة سيادتكم بأنه تم تعديل",
                "chassis": "Chassis Number",
                "motor": "Motor Number",
                "brand": "Car Brand",
                "model": "Car Model",
                "customer": "Customer",
                "body":"WOW",
                "ending": "وتفضلوا بقبول فائق الاحترام والتقدير،،،،",
            }}
        return language_dic[lang]
