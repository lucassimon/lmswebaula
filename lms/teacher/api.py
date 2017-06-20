# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

from lms.teacher.containers import *

from lms.teacher.rpc import (
    RPC as TeacherRPC
)


from lms.teacher.parse import (
    TeacherParse
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Teacher.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = TeacherRPC(
            login=login,
            passport=passport
        )

    def bind_class(self, data_rq):
        """
        Associa o corpo docente a uma turma
        """

        raise NotImplementedError

    def bind_class_trail(self, data_rq):
        """
        Associa um corpo docente a uma turma de trilha.
        """

        raise NotImplementedError

    def bind_coordination(self, data_rq):
        """
        Realiza a associação entre o corpo docente e a coordenação.
        """

        raise NotImplementedError

    def bind_course(self, data_rq):
        """
        Associa o corpo docente a um curso.
        """

        raise NotImplementedError

    def bind_profile_access(self, data_rq):
        """
        Associa o usuário gestor do corpo docente aos itens do perfil.
        """

        raise NotImplementedError

    def change_password(self, data_rq):
        """
        Altera a senha do corpo docente
        """

        raise NotImplementedError

    def delete_profile_access(self, data_rq):
        """
        Deleta todos os perfis de acesso do usuário gestor
        associado ao corpo docente
        """

        raise NotImplementedError

    def get_all(self, paginate_rq):
        """
        Retorna todos os estudantes
        """

        if not isinstance(paginate_rq, GetAllRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        response = None

        try:
            response = self.rpc.get_all(paginate_rq)
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

        data = TeacherParse.get_all(response)

        # Retornar o teacher response

        data_rs = GetAllTeacherRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_all_paper_teacher(self, data_rq):
        """
        Retorna todos os papeis para o corpo docente
        """

        raise NotImplementedError

    def get_by_id(self, data_rq):
        """
        Retorna o estudande de acordo com o ID
        """

        if not isinstance(data_rq, GetByIdRQ):
            raise ValueError(
                "Não existe uma instancia para os dados de estudante"
            )

        response = None

        try:
            response = self.rpc.get_by_id(data_rq)
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

        data = TeacherParse.get_all(response)

        # Retornar o teacher response

        data_rs = GetAllTeacherRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def save(self, teacher_rq):
        """
        Cria/Atualiza um professor
        """

        if not isinstance(teacher_rq, SaveRQ):
            raise ValueError(
                "Não existe uma instância para os dados do professor"
            )

        response = None

        try:
            response = self.rpc.save(teacher_rq)
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

    def unbound_class(self, data_rq):
        """
        Desvincula o corpo docente da turma
        """

        raise NotImplementedError

    def unbound_class_trail(self, data_rq):
        """
        Associa um corpo docente a uma turma de trilha
        """

        raise NotImplementedError

    def unbound_coordination(self, data_rq):
        """
        Desvincula o corpo docente da coordenação
        """

        raise NotImplementedError

    def unbound_course(self, data_rq):
        """
        Desvincula o corpo docente do curso
        """

        raise NotImplementedError
