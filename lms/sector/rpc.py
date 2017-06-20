# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from zeep import Client
from lms.sector.containers import *

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
            response = request.service.GetById(
                passport=self._passport,
                lmsSectorId=data.lms_sector_id,
            )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, SaveRQ):
            raise ValueError(
                "Não existe dados para o Setor"
            )

        request = Client(self._login.url)

        array_dto = request.get_type('ns4:ArrayOfSectorDTO')

        data_dto = request.get_type('ns4:SectorDTO')

        data = data_dto(
            Name=data.name,
            SectorId=data.sector_id,
        )

        data_list = array_dto(SectorDTO=data)

        try:
            response = request.service.Save(
                passport=self._passport,
                sectorListDTO=data_list
            )

        except Exception as e:
            raise e

        return response
