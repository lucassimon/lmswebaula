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

from lms.student.containers import *

from lms.student.rpc import (
    RPC as StudentRPC
)


from lms.student.parse import (
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
        except ConnectionError as e:
            pytest.set_trace()
        except NewConnectionError as e:
            pytest.set_trace()
        except HTTPError as e:
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

        data = StudentParse.get_all(response)

        data_rs = SaveRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def bind_branch_manager(self, data_rq):
        """
        Associa um aluno com gerente filial
        """

        raise NotImplementedError

    def bind_level(self, data_rq):
        """
        Associa o usuário ao Level (PDINivel)
        """

        raise NotImplementedError

    def bind_sector(self, data_rq):
        """
        Associa o usuário ao Setor
        """

        raise NotImplementedError

    def bind_segment(self, data_rq):
        """
        Atribui segmento ao aluno
        """

        raise NotImplementedError

    def get_by_login(self, data_rq):
        """
        Recupera um aluno pelo login no LMS
        """

        raise NotImplementedError

    def get_login_integred_by_user(self, data_rq):
        """
        Recupera a url de autenticação do LMS
        """

        raise NotImplementedError

    def get_password_reminder(self, data_rq):
        """
        Recupera lembrete de senha
        """

        raise NotImplementedError

    def get_segment_main(self, data_rq):
        """
        Recupera o segmento principal do aluno
        """

        raise NotImplementedError

    def get_student_segment(self, data_rq):
        """
        Recupera uma associação entre o aluno e o segmento
        """

        raise NotImplementedError

    def send_password_by_email(self, data_rq):
        """
        Envia senha do aluno por E-mail
        """

        raise NotImplementedError

    def student_lms_id(self, data_rq):
        """
        Recupera o código do usuário na webAula pelo seu login
        """

        raise NotImplementedError

    def teste_date(self, data_rq):
        """
        Recupera o código do usuário na webAula pelo seu login
        """

        raise NotImplementedError

    def unbound_all_level(self, data_rq):
        """
        Retira o aluno de todos os niveis vinculados a ele
        """

        raise NotImplementedError

    def unbound_all_sector(self, data_rq):
        """
        Retira o aluno de todos os setores
        """

        raise NotImplementedError

    def unbound_branch_manager(self, data_rq):
        """
        Retira a associação do aluno como gerente da filial
        """

        raise NotImplementedError

    def unbound_level(self, data_rq):
        """
        Retira a associação do aluno no Level (PDINivel)
        """

        raise NotImplementedError

    def unbound_sector(self, data_rq):
        """
        Retira a associação do aluno no Setor
        """

        raise NotImplementedError

    def unbound_segment(self, data_rq):
        """
        Retira o segmento do aluno
        """

        raise NotImplementedError

    def upload_file(self, data_rq):
        """
        Recebe a foto do usuário
        """

        raise NotImplementedError
