# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.containers.login import LoginRQ

from lmswebaula.lms.course.containers import *

from lmswebaula.lms.course.rpc import (
    RPC as CourseRPC
)

from lmswebaula.lms.course.parse import (
    CourseParse
)


class API(object):
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

    def _verifica_exception(self, res, execption_class=Exception):

        if res['hasError']:
            raise execption_class(res['Msg'])

    def get_all(self, paginate_rq):
        """
        Retorna todos os cursos
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

        data = CourseParse.get_all(response)

        # Retornar o course response

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
