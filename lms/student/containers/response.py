# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class StudentDTO(object):

    _address = None
    _admission_date = None
    _branch_id = None
    _cep = None
    _cpf = None
    _celular = None
    _city = None
    _company = None
    _complement = None
    _ddd = None
    _date_import = None
    _date_of_birth = None
    _date_of_registration = None
    _department_id = None
    _district = None
    _email = None
    _field1 = None
    _field2 = None
    _field3 = None
    _field4 = None
    _foreing_student = False
    _free_table_1_id = None
    _free_table_2_id = None
    _free_table_5_id = None
    _job_id = None
    _lms_branch_id = None
    _lms_department_id = None
    _lms_free_table_1 = None
    _lms_free_table_2 = None
    _lms_free_table_5 = None
    _lms_job_id = None
    _lms_marital_status_id = None
    _lms_schooling_id = None
    _lms_student_id = None
    _lms_team_id = None
    _level_list = None
    _login = None
    _marital_status_id = None
    _name = None
    _nick_name = None
    _number = None
    _password = None
    _registration = None
    _schooling_id = None
    _sector_list = None
    _sex = None
    _state_abbreviation = None
    _status = True
    _student_id = None
    _team_id = None

    def __init__(
        self,
        lms_student_id,
        cpf,
        email,
        login,
        name,
        sex,
        date_of_birth=None,
        status=None
    ):
        self._lms_student_id = lms_student_id
        self._cpf = cpf
        self._date_of_birth = date_of_birth
        self._email = email
        self._login = login
        self._name = name
        self._sex = sex
        self._status = status

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):

        self._cpf = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):

        self._date_of_birth = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        self._email = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):

        self._login = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):

        self._sex = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        self._status = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):

        self._password = value

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        self._lms_student_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        self._student_id = value

    def convert_to_post(self):

        return {
            'AdmissionDate': self._admission_date,
            'BranchId': self._branch_id,
            'CEP': self._cep,
            'CPF': self._cpf,
            'Celular': self._celular,
            'City': self._city,
            'Company': self._company,
            'Complement': self._complement,
            'DDD': self._ddd,
            'DateOfBirth': self._date_of_birth,
            'DepartmentId': self._department_id,
            'District': self._district,
            'Email': self._email,
            'ForeingStudent': False,
            'JobId': self._job_id,
            'LMSBranchId': self._lms_branch_id,
            'LMSDepartmentId': self._lms_department_id,
            'LMSJobId': self._lms_job_id,
            'LMSMaritalStatusId': self._lms_marital_status_id,
            'LMSSchoolingId': self._lms_schooling_id,
            'LMSStudentId': self._lms_schooling_id,
            'LMSTeamId': self._lms_team_id,
            'Login': self._email,
            'MaritalStatusId': self._marital_status_id,
            'Name': self._name,
            'NickName': self._nick_name,
            'Number': self._number,
            'Password': self._password,
            'Registration': self._registration,
            'SchoolingId': self._schooling_id,
            'Sex': self._sex,
            'StateAbbreviation': self._state_abbreviation,
            'StudentId': self._student_id,
            'TeamId': self._team_id
        }
