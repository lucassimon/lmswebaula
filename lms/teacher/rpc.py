# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.teacher.containers import *

import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})


class RPC(object):

    formato_data = '%Y-%m-%d'
    formato_hora = '%H:%M:%S'

    def __init__(self, login, passport):

        self._login = login
        self._passport = passport

    def get_all(self, paginate):

        if not isinstance(paginate, GetAllRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        request = Client(self._login.url)

        try:
            response = request.service.GetAll(
                passport=self._passport,
                page=paginate.page,
                pageSize=paginate.page_size
            )
        except Exception as e:
            raise e

        return response

    def get_by_id(self, data):

        if not isinstance(data, GetByIdRQ):
            raise ValueError(
                "Não existe uma instancia para os dados de estudante"
            )

        request = Client(self._login.url)

        try:
            response = request.service.GetById(
                passport=self._passport,
                lmsTeacherId=data.lms_teacher_id,
            )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, SaveRQ):
            raise ValueError(
                "Não existe dados para o professor"
            )

        request = Client(self._login.url)

        array_schema = request.get_type('ns2:ArrayOfTeacherDTO')

        item_schema = request.get_type('ns2:TeacherDTO')

        item = item_schema(
            TeacherId=data.teacher_id,
            Name=data.name,
            Email=data.email,
            Password=data.password,
            Status=data.status,
            NumberOfAttendance=data.number_of_attendance,
            MaxAttendance=data.max_attendance,
            ReceiveEmailForum=data.receive_email_forum,
            Job=data.job,
            Cpf=data.cpf,
            Coordinator=data.coordinator
        )

        items = array_schema(TeacherDTO=item)

        try:
            response = request.service.Save(
                passport=self._passport,
                teacherListDTO=items
            )

        except Exception as e:
            raise e

        return response
