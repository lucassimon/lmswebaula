# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.student.containers import *

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

            if data.lms_student_id:
                response = request.service.GetById(
                    passport=self._passport,
                    lmsStudentId=data.lms_student_id,
                )
            elif data.student_id:
                response = request.service.GetById(
                    passport=self._passport,
                    studentId=data.student_id,
                )
            else:
                raise ValueError(
                    "Precisa-se de um valor para pesquisar o estudante"
                )
        except Exception as e:
            raise e

        return response

    def set_status(self, status):

        if not isinstance(status, StatusRQ):
            raise ValueError(
                "Não existe uma instância para os dados do status"
            )

        request = Client(self._login.url)

        try:
            response = request.service.SetStatus(
                passport=self._passport,
                lmsStudentId=status.lms_student_id,
                active=status.active
            )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, SaveRQ):
            raise ValueError(
                "Não existe dados para o estudante"
            )

        request = Client(self._login.url)

        array_student_dto = request.get_type('ns5:ArrayOfStudentDTO')

        student_dto = request.get_type('ns5:StudentDTO')

        student = student_dto(
            Registration=data.registration,
            Name=data.name,
            Email=data.email,
            CPF=data.cpf,
            Status=data.status,
            Password=data.password,
            StudentId=data.student_id
        )

        student_list = array_student_dto(StudentDTO=student)

        try:
            response = request.service.Save(
                passport=self._passport,
                studentListDTO=student_list
            )

        except Exception as e:
            raise e

        return response
