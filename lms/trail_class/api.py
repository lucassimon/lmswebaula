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

from lms.trail_class.containers import *

from lms.trail_class.rpc import (
    RPC as TrailRPC
)


from lms.trail_class.parse import (
    TrailClassParse
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/TrailClass.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = TrailRPC(
            login=login,
            passport=passport
        )

    def associate_coaches_in_trail_class(self, data_rq):
        """
        Recupera o grupo pelo nome
        """

        raise NotImplementedError

    def get(self, data_rq):
        """
        Recupera uma turma de trilha
        """

        if not isinstance(data_rq, GetRQ):
            raise ValueError(
                "Não existe uma instância para os dados da trilha"
            )

        response = None

        try:
            response = self.rpc.get(data_rq)
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
                exception=e
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

        data = TrailClassParse.get_all(response)

        # Retornar o trail response

        data_rs = GetRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def save(self, data_rq):
        """
        Salva uma turma de trilha
        """

        if not isinstance(data_rq, SaveRQ):
            raise ValueError(
                "Não existe uma instância para os dados do professor"
            )

        response = None

        try:
            response = self.rpc.save(data_rq)
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
                exception=e
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

        data = TeacherParse.get_all(response)

        data_rs = SaveRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs
