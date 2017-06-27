# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from zeep import Client
from lms.trail.containers import *

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

    def get_trail(self, data):

        if not isinstance(data, GetTrailRQ):
            raise ValueError(
                "Não existe uma instancia para os dados de trilha"
            )

        request = Client(self._login.url)

        try:
            response = request.service.GetTrail(
                passport=self._passport,
                trailId=data.trail_id,
            )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, SaveRQ):
            raise ValueError(
                "Não existe dados para a trilha"
            )

        request = Client(self._login.url)

        array_schema = request.get_type('ns2:ArrayOfTrailDTO')

        item_schema = request.get_type('ns2:TrailDTO')

        item = item_schema(
            TrailId=data.trail_id,
            Name=data.name,
            Description=data.description,
            LMSActivityGroupId=data.lms_activity_group_id,
            LMSGroupId=data.lms_group_id,
            GroupId=data.group_id,
            Active=data.active,
            Hours=data.hours,
        )

        items = array_schema(TrailDTO=item)

        try:
            response = request.service.Save(
                passport=self._passport,
                trailListDTO=items
            )

        except Exception as e:
            raise e

        return response

    def get_all_courses_ordered_by_name(self, data):

        if not isinstance(data, GetAllCoursesOrderedByNameRQ):
            raise ValueError(
                "Não existe dados para a pesquisa em Grupos de Trilha"
            )

        request = Client(self._login.url)

        response = None

        try:
            response = request.service.GetAllCoursesOrderedByName(
                passport=self._passport,
                page=data.page,
                pageSize=data.page_size
            )
        except Exception as e:
            raise e

        return response

    def enroll_student_in_default_discipline(self, data):

        if not isinstance(data, EnrollStudentInDefaultDisciplineRQ):
            raise ValueError(
                "Não existe uma instância para "
                "matricular o aluno em uma disciplina"
            )
        request = Client(self._login.url)

        item_schema = request.get_type('ns2:DateTimeOffset')

        initial_access_date = item_schema(
            DateTime=data.initial_access_date,
            OffsetMinutes=0
        )

        final_access_date = item_schema(
            DateTime=data.final_access_date,
            OffsetMinutes=0
        )

        response = None

        try:
            response = request.service.EnrollStudentInDefaultDiscipline(
                passport=self._passport,
                lmsStudentId=data.lms_student_id,
                disciplineId=data.discipline_id,
                courseId=data.course_id,
                initialAccessDate=initial_access_date,
                finalAccessDate=final_access_date
            )

        except Exception as e:

            raise e

        return response
