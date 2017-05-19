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
from lms.core.containers.error import ErrorRS


from lms.sector.containers import *
from lms.sector.parse import SectorParse
from lms.sector.rpc import (
    RPC
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Sector.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = RPC(
            login=login,
            passport=passport
        )

    def get_all(self, data_rq):
        """
        Retorna todos os cargos
        """
        if not isinstance(data_rq, GetAllRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        try:
            response = self.rpc.get_all(data_rq)
        except ConnectionError as e:
            pytest.set_trace()
        except NewConnectionError as e:
            pytest.set_trace()
        except HttpError as e:
            pytest.set_trace()
        except Exception as e:
            pytest.set_trace()

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

        data = SectorParse.get_all(response)

        # Retornar o course response

        data_rs = GetAllSectorRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_by_id(self, data_rq):
        """
        Recupera um cargo pelo código.
        """
        if not isinstance(data_rq, GetByIdRQ):
            raise ValueError(
                "Não existe uma instancia para os dados do curso"
            )

        try:
            response = self.rpc.get_by_id(data_rq)
        except ConnectionError as e:
            pytest.set_trace()
        except NewConnectionError as e:
            pytest.set_trace()
        except HttpError as e:
            pytest.set_trace()
        except Exception as e:
            pytest.set_trace()

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

        data = SectorParse.get_all(response)

        # Retornar o response

        data_rs = GetAllSectorRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def save(self, data_rq):
        """
        Cria/Atualiza um departamento/Setor
        """

        if not isinstance(data_rq, SaveRQ):
            raise ValueError(
                "Não existe uma instância para os dados do setor"
            )

        try:
            response = self.rpc.save(data_rq)
        except ConnectionError as e:
            pytest.set_trace()
        except NewConnectionError as e:
            pytest.set_trace()
        except HttpError as e:
            pytest.set_trace()
        except Exception as e:
            pytest.set_trace()

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

        data = SectorParse.get_all(response)

        data_rs = SaveRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs
