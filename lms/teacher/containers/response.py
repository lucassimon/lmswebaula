# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class TeacherDTO(object):

    _lms_teacher_id = None
    _teacher_id = None
    _name = None
    _email = None
    _password = None
    _status = False
    _number_of_attendance = None
    _max_attendance = None
    _recive_email_forum = False
    _job = None
    _cpf = None
    _coordinator = False
    _payment_methods = None

    def __init__(
        self,
        lms_teacher_id,
        cpf,
        email,
        password,
        job,
        coordinator,
        name,
        status,
        teacher_id=None
    ):
        if not isinstance(lms_teacher_id, six.integer_types):
            raise ValueError(
                'O lms id do professor precisa ser um inteiro'
            )

        self._lms_teacher_id = lms_teacher_id
        self._cpf = cpf
        self._email = email
        self._name = name
        self._status = status
        self._job = job
        self._coordinator = coordinator

        if teacher_id:

            if not isinstance(teacher_id, six.integer_types):
                raise ValueError(
                    'O id do professor precisa ser um inteiro'
                )

            self._teacher_id = teacher_id

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):

        self._cpf = value

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
    def lms_teacher_id(self):
        return self._lms_teacher_id

    @lms_teacher_id.setter
    def lms_teacher_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do professor precisa ser um inteiro'
            )

        self._lms_teacher_id = value

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do professor precisa ser um inteiro'
            )

        self._teacher_id = value
