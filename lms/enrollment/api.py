# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.api import APIBase
from lmswebaula.lms.core.containers.login import LoginRQ
from lmswebaula.lms.core.containers.error import ErrorRS

from lmswebaula.lms.enrollment.containers import *

from lmswebaula.lms.enrollment.rpc import RPC


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Enrollment.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = RPC(
            login=login,
            passport=passport
        )

    def enrollment_course(self, data_rq):
        """
        Matricula o aluno na turma de curso
        """

        if not isinstance(data_rq, EnrollmentCourseRQ):
            raise ValueError(
                "Não existe uma instância para os dados da matricula"
            )

        try:
            response = self.rpc.enrollment_course(data_rq)
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

        self._verifica_exception(response)

        res = EnrollmentCourseRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg']
        )

        return res

    def set_status_in_class(self, data_rq):
        """
        Altera o status de uma matricula.
        """

        if not isinstance(data_rq, SetStatusInClassRQ):
            raise ValueError(
                "Não existe uma instância para os dados do status"
            )

        try:
            response = self.rpc.set_status_in_class(data_rq)
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

        res = SetStatusInClassRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg']
        )

        return res
