# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from requests.exceptions import (
    Timeout,
    HTTPError,
    ConnectionError,
    ProxyError,
    SSLError,
    ConnectTimeout,
    ReadTimeout,
    TooManyRedirects,
    RetryError
)

from lms.core.api import APIBase
from lms.core.containers.login import LoginRQ
from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.enrollment.containers import *

from lms.enrollment.rpc import RPC


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

        response = None

        try:
            response = self.rpc.enrollment_course(data_rq)
        except ValueError as e:
            return ErrorRS(
                error=True,
                msg=e.message,
            )
        except (
            Timeout, HTTPError, ConnectionError,
            ProxyError, SSLError, ConnectTimeout,
            ReadTimeout, TooManyRedirects, RetryError
        ) as e:
            return ConnectionExceptionRS(
                error=True,
                msg=e.message,
                exception=e
            )
        except Exception as e:
            return ExceptionRS(
                error=True,
                msg=e.message,
            )

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

        response = None

        try:
            response = self.rpc.set_status_in_class(data_rq)
        except ValueError as e:
            return ErrorRS(
                error=True,
                msg=e.message,
            )
        except (
            Timeout, HTTPError, ConnectionError,
            ProxyError, SSLError, ConnectTimeout,
            ReadTimeout, TooManyRedirects, RetryError
        ) as e:
            return ConnectionExceptionRS(
                error=True,
                msg=e.message,
                exception=e
            )
        except Exception as e:
            return ExceptionRS(
                error=True,
                msg=e.message,
            )

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

    def checks_student_enrolled_in_trail_class(self, data_rq):
        """
        Verifica se o aluno está matriculado na turma de trilha
        """

        raise NotImplementedError

    def checks_student_enrolled_in_trail_default_class(self, data_rq):
        """
        Verifica se o aluno está matriculado na turma automatica da trilha
        """

        raise NotImplementedError

    def enrollment_automatic_class_by_course(self, data_rq):
        """
        Realiza a matricula do aluno na turma automatica do curso
        """

        raise NotImplementedError

    def enrollment_program(self, data_rq):
        """
        Matricula um aluno em uma turma de programa
        """

        raise NotImplementedError

    def enrollment_trail(self, data_rq):
        """
        Matricula o aluno na turma de trilha

        """

        raise NotImplementedError

    def enrollment_trail_trail_with_days_as_period_access(self, data_rq):
        """
        Matricula o aluno na trilha e recupera o prazo em dias sugeridos
        para calcular o prazo de acesso
        """

        raise NotImplementedError

    def get_enrollment_course(self, data_rq):
        """
        Recupera as matriculas aplicando os filtros informados
        """

        raise NotImplementedError

    def get_trails_history_by_class_period(self, data_rq):
        """
        Retorna os historicos de trilhas de acordo com o tipo de pesquisa
        em um determinado periodo

        """

        raise NotImplementedError

    def updat_term_enroll_by_term_course(self, data_rq):
        """
        Altera o prazo de acesso da matricula de acordo com o
        prazo de acesso do curso

        """

        raise NotImplementedError
