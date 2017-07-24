# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six

from lms.core.containers.response import (
    SuccessContainerResponse
)


class UpdateRQ(object):

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
        lms_student_id=None,
        student_id=None,
    ):

        if lms_student_id:
            if not isinstance(student_id, six.integer_types):
                raise ValueError(
                    'O lms_student_id precisa ser um inteiro'
                )

            self._lms_student_id = lms_student_id

        if student_id:

            self._student_id = student_id

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

        self._student_id = value


class UpdateRS(SuccessContainerResponse):

    pass
