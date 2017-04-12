# -*- coding: utf-8 -*-


from lmswebaula.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class StudentRQ(object):

    _lms_student_id = ''
    _student_id = ''
    _registration = ''
    _login = ''
    _name = ''
    _email = ''
    _sex = ''
    _admission_date = ''
    _cpf = ''
    _status = ''
    _password = ''
    _date_import = ''
    _address = ''
    _number = ''
    _complement = ''
    _district = ''
    _city = ''
    _state_abbreviation = ''
    _cep = ''
    _date_of_birth = ''
    _ddd = ''
    _celular = ''
    _nickname = ''
    _company = ''

    def __init__(self):
        pass


class StudentRS(ContainerResponse):

    _student = None
    _errors = []

    def __init__(self):

        pass
