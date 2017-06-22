# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lms.competence.containers import *

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
                "Não existe uma instancia para os dados o setor"
            )

        request = Client(self._login.url)

        try:
            if data.lms_competence_id:
                response = request.service.GetById(
                    passport=self._passport,
                    lmsCompetenceId=data.lms_competence_id,
                )
            elif data.competence_id:
                response = request.service.GetById(
                    passport=self._passport,
                    competenceId=data.competence_id,
                )
            else:
                raise ValueError(
                    "Precisamos de um id para pesquisar a competencia"
                )

        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, SaveRQ):
            raise ValueError(
                "Não existe dados para o Nivel"
            )

        request = Client(self._login.url)

        array_dto = request.get_type('ns4:ArrayOfCompetenceDTO')

        data_dto = request.get_type('ns4:CompetenceDTO')

        data = data_dto(
            Name=data.name,
            CompetenceId=data.competence_id,
        )

        data_list = array_dto(CompetenceDTO=data)

        try:
            response = request.service.Save(
                passport=self._passport,
                competenceListDTO=data_list
            )

        except Exception as e:
            raise e

        return response
