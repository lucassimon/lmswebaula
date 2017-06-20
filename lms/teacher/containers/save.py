# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse
)


class SaveRQ(object):

    _lms_teacher_id = None
    _teacher_id = None
    _name = None
    _email = None
    _password = None
    _status = False
    _number_of_attendance = 0
    _max_attendance = 0
    _receive_email_forum = False
    _job = None
    _cpf = None
    _coordinator = False
    _payment_methods = None

    def __init__(
        self,
        teacher_id,
        name,
        email,
        password,
        status,
        job,
        cpf
    ):

        if not isinstance(teacher_id, six.integer_types):
            raise ValueError(
                'O id do professor precisa ser um inteiro'
            )

        self._teacher_id = teacher_id
        self._name = name
        self._email = email
        self._password = password
        self._status = status
        self._job = job
        self._cpf = cpf

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

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

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):

        self._password = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        self._status = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):

        self._job = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):

        self._cpf = value

    @property
    def number_of_attendance(self):
        return self._number_of_attendance

    @number_of_attendance.setter
    def number_of_attendance(self, value):

        self._number_of_attendance = value

    @property
    def max_attendance(self):
        return self._max_attendance

    @max_attendance.setter
    def max_attendance(self, value):

        self._max_attendance = value

    @property
    def receive_email_forum(self):
        return self._receive_email_forum

    @receive_email_forum.setter
    def receive_email_forum(self, value):

        self._receive_email_forum = value

    @property
    def coordinator(self):
        return self._coordinator

    @coordinator.setter
    def coordinator(self, value):

        self._coordinator = value

    @property
    def payment_methods(self):
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, value):

        self._payment_methods = value


class SaveRS(SuccessContainerResponse):

    pass
