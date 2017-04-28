# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class SaveRQ(object):

    _lms_student_id = ''
    _student_id = ''
    _registration = ''
    _login = ''
    _name = ''
    _email = ''
    _sex = ''
    _admission_date = ''
    _cpf = ''
    _status = True
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

    def __init__(
        self,
        name,
        email,
        cpf,
        password,
        student_id,
        registration=None
    ):
        if not isinstance(student_id, six.integer_types):
            raise ValueError(
                'O student_id precisa ser um inteiro'
            )

        self._name = name
        self._email = email
        self._cpf = cpf
        self._password = password
        self._student_id = student_id

        if registration is None:
            self._registration = cpf
        else:
            self._registration = registration

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        self._email = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):

        self._cpf = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):

        self._password = value

    @property
    def registration(self):
        return self._registration

    @registration.setter
    def registration(self, value):

        self._registration = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        self._status = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O student_id precisa ser um inteiro'
            )

        self._student_id = value


class SaveRS(ContainerResponse):
    """
    Resposta do metodo save
    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'Os estudantes precisam estar em uma lista'
            )

        self._data_list = data
        self._has_error = error
        self._guid = guid
        self._msg = msg

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):

        if not isinstance(value, list):
            raise ValueError(
                'Os estudantes precisam estar em uma lista'
            )

        self._data_list = value
