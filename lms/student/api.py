# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.api import APIBase
from lmswebaula.lms.core.containers.login import LoginRQ

from lmswebaula.lms.student.containers import *

from lmswebaula.lms.student.rpc import (
    RPC as StudentRPC
)

from lmswebaula.lms.student.containers.students import (
    StudentRS
)

from lmswebaula.lms.student.parse import (
    StudentParse
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Student.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = StudentRPC(
            login=login,
            passport=passport
        )

    def get_all(self, paginate_rq):
        """
        Retorna todos os estudantes
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

        data = StudentParse.get_all(response)

        # Retornar o student response

        data_rs = GetAllStudentRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_by_id(self, data_rq):
        """
        Retorna o estudande de acordo com o ID
        """

        if not isinstance(data_rq, GetByIdRQ):
            raise ValueError(
                "Não existe uma instancia para os dados de estudante"
            )

        try:
            response = self.rpc.get_by_id(data_rq)
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        self._verifica_exception(response)

        # tratar os dados

        data = StudentParse.get_all(response)

        # Retornar o student response

        data_rs = GetAllStudentRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def set_status(self, status_rq):
        """
        Seta o status para ativo ou inativo de acordo
        com o Id do estudante
        """

        if not isinstance(status_rq, StatusRQ):
            raise ValueError(
                "Não existe uma instancia para os dados do status"
            )

        try:
            response = self.rpc.set_status(status_rq)
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        self._verifica_exception(response)

        # Retornar o student response

        data_rs = StatusRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
        )

        return data_rs

    def save(self, student_rq):
        """
        Cria/Atualiza um aluno
        """

        if not isinstance(student_rq, SaveRQ):
            raise ValueError(
                "Não existe uma instância para os dados do estudante"
            )

        try:
            response = self.rpc.save(student_rq)
        except Exception as e:
            raise e

        self._verifica_exception(response)

        data = StudentParse.get_all(response)

        data_rs = SaveRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs
