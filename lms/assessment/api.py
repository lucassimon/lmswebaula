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
from lms.core.containers.pagination import (
    PaginationParse
)


from lms.assessment.containers import *
from lms.assessment.rpc import (
    RPC
)
from lms.assessment.parse import (
    NoteReviewParse
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Assessment

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Assessment.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(
            passport,
            url=self.ENDPOINT
        )

        self.rpc = RPC(
            login=login,
            passport=passport
        )

    def bind_question(self):
        """
        Associa uma questão a um topico
        """

        raise NotImplementedError

    def get_assessment_class_room(self):
        """
        Recupera uma avaliação presencial
        """

        raise NotImplementedError

    def get_assessment_online(self):
        """
        Recupera uma avaliação online
        """

        raise NotImplementedError

    def get_delivered_assessment(self):
        """
        Recupera dados das ultimas avaliações realizadas de turmas
        de cursos de acordo com os filtros informados
        """

        raise NotImplementedError

    def get_delivered_assessment_trail(self, data_rq):
        """
        Recupera dados das avaliações realizadas de turmas de
        trilhas de acordo com os filtros informados.
        """

        if not isinstance(data_rq, GetDeliveredAssessmentTrailRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da busca de nota"
            )

        response = None

        try:
            response = self.rpc.get_delivered_assessment_trail(data_rq)
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

        data = NoteReviewParse.parse(response)

        # Retornar o student response

        data_rs = GetDeliveredAssessmentTrailRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        # insere os dados de paginação
        data_rs.pagination = PaginationParse.parse(response['PaginationInfo'])

        return data_rs

    def save_assessment_class_room(self):
        """
        Salva uma avaliação presencial
        """

        raise NotImplementedError

    def save_assessment_online(self):
        """
        Salva/Atualiza uma avaliação online
        """

        raise NotImplementedError
