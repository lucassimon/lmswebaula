# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lmswebaula.lms.core.containers.response import (
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
        cpf,
        email,
        login,
        name,
        sex,
        date_of_birth=None,
        status=None
    ):

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

    def convert_to_post(self):

        return {
            'Name': self.name,
            'Email': self.email,
            'CPF': self.cpf,
        }


class StudentRS(ContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Student&m=GetAll

    {
        Guid: 8c0a5920-c24b-4ded-b59b-d5085268cd96
        Msg: A pagina deve ser maior que 0,
        PaginationInfo: {
            NumberOfPages: None,
            Page: None,
            PageSize: None,
            TotalAmount: None
        },
        hasError: True,
        ErrorList: {
            EntityId: []
        },
        StudentListDTO: {
            StudentDTO: []
        },
            TranscriptListDTO: {
            StudentCourseSituationDTO: []
        }
    }
    """

    _student_list = []

    def __init__(self, error=True, guid='', msg='', students=[]):

        self._has_error = error
        self._guid = guid
        self._msg = msg
        self._student_list = students

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):

        self._has_error = value

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):

        self._guid = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):

        self._msg = value

    @property
    def student_list(self):
        return self._student_list

    @student_list.setter
    def student_list(self, value):

        if not isinstance(value, list):
            raise ValueError(
                'Os estudantes precisa ser uma lista'
            )

        self._student_list = value
