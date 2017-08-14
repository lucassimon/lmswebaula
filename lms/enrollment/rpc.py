# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.enrollment.containers import *

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

    def checks_student_enrolled_in_trail_class(self, data_rq):

        if not isinstance(data_rq, EnrolledInTrailClassRQ):
            raise ValueError(
                "Não existe uma instância para os dados da aluno matriculado"
            )

        request = Client(self._login.url)

        response = None

        try:

            if data_rq.trail_class_id:
                response = request.service.ChecksStudentEnrolledInTrailClass(
                    passport=self._passport,
                    userId=data_rq.user_id,
                    trailClassId=data_rq.trail_class_id,
                )
            elif data_rq.lms_trail_class_id:

                response = request.service.ChecksStudentEnrolledInTrailClass(
                    passport=self._passport,
                    userId=data_rq.user_id,
                    lmsTrailClassId=data_rq.lms_trail_class_id,
                )
            else:
                raise ValueError(
                    "Não existe um id de trilha para pesquisa"
                )

        except Exception as e:
            raise e

        return response

    def checks_student_enrolled_in_trail_default_class(self, data_rq):

        if not isinstance(data_rq, EnrolledInTrailDefaultClassRQ):
            raise ValueError(
                "Não existe uma instância para os dados da aluno matriculado"
            )

        request = Client(self._login.url)

        response = None

        try:

            if data_rq.trail_id:
                response = request.service.ChecksStudentEnrolledInTrailDefaultClass(
                    passport=self._passport,
                    userId=data_rq.user_id,
                    trailId=data_rq.trail_id,
                )
            elif data_rq.lms_trail_id:
                response = request.service.ChecksStudentEnrolledInTrailDefaultClass(
                    passport=self._passport,
                    userId=data_rq.user_id,
                    lmsTrailId=data_rq.lms_trail_id,
                )
            else:
                raise ValueError(
                    "Não existe um id de trilha para pesquisa"
                )
        except Exception as e:
            raise e

        return response

    def get_trails_history_by_class_period(self, data_rq):

        if not isinstance(data_rq, GetTrailsHistoryByClassPeriodRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        request = Client(self._login.url)

        pytest.set_trace()

        data = {
            'passport': self._passport,
            'from': data_rq.ffrom,
            'to': data_rq.to,
            'page': data_rq.page,
            'pageSize': data_rq.page_size,
            'typeSearch': data_rq.type_search
        }

        try:
            response = request.service.GetTrailsHistoryByClassPeriod(
                **data
            )
        except Exception as e:
            raise e

        return response
