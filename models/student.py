# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = "Student Model"
    f_name = fields.Char('Fist name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    registration_date = fields.Date('Registration Date')
    email = fields.Char()
    phone = fields.Char()
    department_id =  fields.Many2one(comodel_name='university.department')
    classroom_id =  fields.Many2one(comodel_name='university.classroom')

    def name_get(self):
        result = []
        for student in self:
            name = ' [ ' + student.classroom_id.classroom_name + ' ] ' + student.f_name + ' ' + student.l_name
            result.append((student.id,name))
        return result
    @api.constrains('birthday','registration_date')
    def check_dates(self):
        if (self.birthday > self.registration_date):
            raise ValueError(" The birth-day exceeds the registration-date ! ")


