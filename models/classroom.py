# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityClassroom(models.Model):
    _name = 'university.classroom'
    _description = "Classsrom Model"
    classroom_name = fields.Char(String = 'name')
    code = fields.Char()
    _rec_name = 'classroom_name'
    student_ids = fields.One2many(comodel_name = 'university.student', inverse_name = 'classroom_id')
    professor_ids = fields.Many2many(comodel_name='university.professor', relation='class_prof_rel', column1='name', column2='f_name')
    subject_ids = fields.Many2many(comodel_name='university.subject', relation='class_subj_rel', column1='classroom_name', column2='f_name')
    numb_prof = fields.Integer("Nombre de Professeurs:", compute = 'compter_prof')
    numb_subj = fields.Integer("Nombre de Matières:", compute = 'compter_subj')
    numb_stud = fields.Integer("Nombre des Étudiants:", compute = 'compter_stud')
    def compter_prof(self):
        self.numb_prof = len(self.professor_ids)
    def compter_subj(self):
        self.numb_subj = len(self.subject_ids)
    def compter_stud(self):
        self.numb_stud = len(self.student_ids)
    @api.onchange('subject_ids')
    def check_number_subjects(self):
        if len(self.subject_ids) > 3:
            return {'warning' : { 'title ': "warning ! ", 'message' : " Number of subjects exceeds limit (3) "}}

        


