# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.api import APIBase
from lmswebaula.lms.core.containers.login import LoginRQ
from lmswebaula.lms.core.containers.error import ErrorRS


from lmswebaula.lms.segment.containers import *

from lmswebaula.lms.segment.rpc import (
    RPC
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Segment.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = RPC(
            login=login,
            passport=passport
        )

    def get_all(self, data_rq):
        """
        Retorna todos os segmentos
        """
        if not isinstance(data_rq, GetAllRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        try:
            response = self.rpc.get_all(data_rq)
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        if self._verifica_response_none(response):
            return ErrorRS(
                error=True,
                msg='Resposta nula ou vazia.'
            )

        if self._verifica_response_has_error(response):

            return ErrorRS(
                error=response['hasError'],
                guid=response['Guid'],
                msg=response['Msg'],
            )

        # tratar os dados

        data = SegmentParse.get_all(response)

        # Retornar o course response

        data_rs = GetAllSegmentRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_by_id(self, data_rq):
        """
        Recupera um segmento pelo código.
        """
        if not isinstance(data_rq, GetByIdRQ):
            raise ValueError(
                "Não existe uma instancia para os dados do curso"
            )

        try:
            response = self.rpc.get_by_id(data_rq)
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        if self._verifica_response_none(response):
            return ErrorRS(
                error=True,
                msg='Resposta nula ou vazia.'
            )

        if self._verifica_response_has_error(response):

            return ErrorRS(
                error=response['hasError'],
                guid=response['Guid'],
                msg=response['Msg'],
            )

        # tratar os dados

        data = SegmentParse.get_all(response)

        # Retornar o response

        data_rs = GetAllSegmentRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_by_description(self, data_rq):
        """
        Recupera os segmentos pelo nome
        """

        pass

    def save(self, data_rq):
        """
        Cria/Atualiza um segmentos
        """

        pass
