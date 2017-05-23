# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.course.containers import *

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
                "Não existe uma instancia para os dados do cursao"
            )

        request = Client(self._login.url)

        try:
            response = request.service.GetById(
                passport=self._passport,
                lmsCourseId=data.lms_course_id,
            )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, SaveRQ):
            raise ValueError(
                "Não existe dados para o curso"
            )

        request = Client(self._login.url)

        array_dto = request.get_type('ns4:ArrayOfCourseDTO')

        data_dto = request.get_type('ns4:CourseDTO')

        data = data_dto(
            Name=data.name,
            NameCourseMenu=data.name_course_menu,
            GroupId=data.group_id,
            CourseId=data.course_id,
            Hours=data.hours,
            Media=data.media,
            Frequency=data.frequency,
            CourseClassTypes=data.course_class_types,
            # SectorList=data.sector_list,
            Status=data.status
        )

        data_list = array_dto(CourseDTO=data)

        try:
            response = request.service.Save(
                passport=self._passport,
                courseListDTO=data_list
            )

        except Exception as e:
            raise e

        return response
