# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.api import APIBase
from lmswebaula.lms.core.containers.login import LoginRQ
from lmswebaula.lms.core.containers.error import ErrorRS


from lmswebaula.lms.course.containers import *

from lmswebaula.lms.course.rpc import (
    RPC as CourseRPC
)

from lmswebaula.lms.course.parse import (
    CourseParse
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Course.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = CourseRPC(
            login=login,
            passport=passport
        )

    def get_all(self, data_rq):
        """
        Retorna todos os cursos
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

        data = CourseParse.get_all(response)

        # Retornar o course response

        data_rs = GetAllCourseRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_by_id(self, data_rq):
        """
        Recupera um curso pelo código.
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

        data = CourseParse.get_all(response)

        # Retornar o response

        data_rs = GetAllCourseRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def save(self, student_rq):
        """
        Cria/Atualiza um curso
        """

        pass
