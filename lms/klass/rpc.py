# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.klass.containers import *

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

            if data.lms_class_id:
                response = request.service.GetById(
                    passport=self._passport,
                    lmsClassId=data.lms_class_id,
                )
            elif data.class_id:
                response = request.service.GetById(
                    passport=self._passport,
                    classId=data.class_id,
                )
            else:
                raise ValueError(
                    "Precisamos de um id para pesquisar a classe"
                )

        except Exception as e:
            raise e

        return response

    def get_by_course_id(self, data):

        if not isinstance(data, GetByCourseIdRQ):
            raise ValueError(
                "Não existe uma instancia para os dados de estudante"
            )

        request = Client(self._login.url)

        try:

            if data.lms_course_id:
                response = request.service.GetByCourseId(
                    passport=self._passport,
                    lmsCourseId=data.lms_course_id,
                )
            elif data.course_id:
                response = request.service.GetByCourseId(
                    passport=self._passport,
                    courseId=data.course_id,
                )
            else:
                raise ValueError(
                    "Precisamos de um id para pesquisar a classe"
                )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        raise NotImplementedError
