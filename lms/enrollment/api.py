# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.containers.login import LoginRQ
from lmswebaula.lms.core.containers.error import ErrorRS

from lmswebaula.lms.enrollment.containers import *

from lmswebaula.lms.enrollment.rpc import RPC


class API(object):
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

    def _verifica_response_none(self, res):

        if res is None:

            return True

        return False

    def _verifica_response_has_error(self, res):

        if res['hasError']:

            return True

        return False

    def _verifica_exception(self, res, execption_class=Exception):

        if res['hasError']:
            raise execption_class(res['Msg'])

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
