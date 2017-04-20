# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.api import APIBase
from lmswebaula.lms.core.containers.login import LoginRQ
from lmswebaula.lms.core.containers.error import ErrorRS

from lmswebaula.lms.klass.containers import *

from lmswebaula.lms.klass.rpc import (
    RPC as KlassRPC
)

from lmswebaula.lms.klass.parse import (
    KlassParse
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Class.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = KlassRPC(
            login=login,
            passport=passport
        )

    def get_all(self, paginate_rq):
        """
        Retorna todos as classes
        """
        if not isinstance(paginate_rq, GetAllRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        try:
            response = self.rpc.get_all(paginate_rq)
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        self._verifica_exception(response)

        # tratar os dados

        data = KlassParse.get_all(response)

        # Retornar o response

        data_rs = GetAllKlassRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_by_id(self, data_rq):
        """
        Recupera uma turma pelo código
        """
        if not isinstance(data_rq, GetByIdRQ):
            raise ValueError(
                "Não existe uma instancia para os dados do estudante"
            )

        try:
            response = self.rpc.get_by_id(data_rq)
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        self._verifica_exception(response)

        # tratar os dados

        data = KlassParse.get_all(response)

        # Retornar o response

        data_rs = GetAllKlassRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_by_course_id(self, data_rq):
        """
        Recupera a lista de turmas de um curso
        """

        if not isinstance(data_rq, GetByCourseIdRQ):
            raise ValueError(
                "Não existe uma instância para os dados da turma"
            )

        try:
            response = self.rpc.get_by_course_id(data_rq)
        except Exception as e:
            raise e

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

        data = KlassParse.get_all(response)

        res = GetAllKlassRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return res

    def save(self, student_rq):
        """
        Cria/Atualiza uma classe
        """

        pass
