# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lmswebaula.lms.enrollment.containers import *

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

    def enrollment_course(self, data_rq):

        if not isinstance(data_rq, EnrollmentCourseRQ):
            raise ValueError(
                "Não existe uma instância para os dados da matricula"
            )

        request = Client(self._login.url)

        now = datetime.datetime.now()

        try:
            response = request.service.EnrollmentCourse(
                passport=self._passport,
                lmsStudentId=data_rq.lms_student_id,
                lmsClassId=data_rq.lms_class_id,
                termAccess=now
            )
        except Exception as e:
            raise e

        return response

    def set_status_in_class(self, data_rq):

        if not isinstance(data_rq, SetStatusInClassRQ):
            raise ValueError(
                "Não existe uma instância para os dados do status"
            )

        request = Client(self._login.url)

        try:
            response = request.service.SetStatusInClass(
                passport=self._passport,
                lmsStudentId=data_rq.lms_student_id,
                lmsClassId=data_rq.lms_class_id,
                status=data_rq.status
            )
        except Exception as e:
            raise e

        return response
