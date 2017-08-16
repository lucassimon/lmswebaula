# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.assessment.containers import *

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

    def get_delivered_assessment_trail(self, data):

        if not isinstance(data, GetDeliveredAssessmentTrailRQ):
            raise ValueError(
                "Não existe uma instancia para os dados de busca de nota"
            )

        request = Client(self._login.url)

        try:

            response = request.service.GetDeliveredAssessmentTrail(
                passport=self._passport,
                trailClassId=data.lms_trail_class_id,
                lmsStudentId=data.lms_student_id,
            )

        except Exception as e:
            raise e

        return response
