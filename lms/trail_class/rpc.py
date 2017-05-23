# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.trail_class.containers import *

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

    def get(self, data):

        if not isinstance(data, GetRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da turma em uma trilha"
            )

        request = Client(self._login.url)

        try:
            response = request.service.Get(
                passport=self._passport,
                trailClassId=data.trail_class_id,
            )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, SaveRQ):
            raise ValueError(
                "Não existe dados para a turma de uma trilha"
            )

        request = Client(self._login.url)

        array_schema = request.get_type('ns2:ArrayOfTrailClassDTO')

        item_schema = request.get_type('ns2:TrailClassDTO')

        item = item_schema(
            LMSTrailClassId=lms_trail_class_id,
            LMSTrailId=data.lms_trail_id,
            TrailId=data.trail_id,
            TrailClassId=data.trail_class_id,
            Name=data.name,
            Description=data.description,
            TimeFrom=data.time_from,
            TimeTo=data.time_to,
            Students=data.students
        )

        if data.lms_activity_group_id:
            item.Vacancies = data.lms_activity_group_id

        items = array_schema(TrailClassDTO=item)

        try:
            response = request.service.Save(
                passport=self._passport,
                trailClassDTOList=items
            )

        except Exception as e:
            raise e

        return response
