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
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Student&m=GetAll

    {
        'Guid': '8c0a5920-c24b-4ded-b59b-d5085268cd96',
        'Msg': 'A pagina deve ser maior que 0',
        'PaginationInfo': {
            'NumberOfPages': None,
            'Page': None,
            'PageSize': None,
            'TotalAmount': None
        },
        'hasError': True,
        'ErrorList': {
            'EntityId': []
        },
        'StudentListDTO': {
            'StudentDTO': []
        },
            'TranscriptListDTO': {
            'StudentCourseSituationDTO': []
        }
    }
    """

    _student = None
    _errors = []

    def __init__(self):

        pass
