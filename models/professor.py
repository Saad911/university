# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
    _name = 'university.professor'
    _description = "Professor MODELE"
    f_name = fields.Char('Fist name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    start_date = fields.Date('Start date')
    email = fields.Char()
    phone = fields.Char()
    department_id =  fields.Many2one(comodel_name='university.department')
    subject_id =  fields.Many2one(comodel_name='university.subject')
    classroom_ids = fields.Many2many(comodel_name = 'university.classroom', relation='prof_class_rel', column1='f_name', column2='name') 
    def name_get(self):
        result = []
        for prof in self:
            name = '[' + prof.department_id.name + ']' + prof.f_name + prof.l_name
            result.append((prof.id, name))
        return result

