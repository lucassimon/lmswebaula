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

from lms.trail.containers import *

from lms.trail.rpc import (
    RPC as TrailRPC
)

from lms.trail.parse import (
    TrailParse, GroupTrailCustomizedParse
)


class API(APIBase):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    _customized = False

    _debug = False

    def __init__(self, passport, login=False, customized=False, debug=False):

        if login is False:

            ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Trail.svc?singleWsdl'
            login = LoginRQ(passport, url=ENDPOINT)

        # Seta o atributo customizado

        self._customized = customized

        self.rpc = TrailRPC(
            login=login,
            passport=passport
        )

    @property
    def customized(self):
        return self._customized

    @customized.setter
    def customized(self, value):
        if not isinstance(value, bool):
            raise ValueError(
                'O atributo customizado precisa ser um booleano'
            )

        self._customized = value

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        if not isinstance(value, bool):
            raise ValueError(
                'O modo debug precisa ser um booleano'
            )

        self._debug = value

    def get_activity_group_by_name(self, data_rq):
        """
        Recupera o grupo pelo nome
        """

        raise NotImplementedError

    def get_trail(self, data_rq):
        """
        Recupera a trilha pelo seu código no sistema legado
        """

        if not isinstance(data_rq, GetByIdRQ):
            raise ValueError(
                "Não existe uma instância para os dados da trilha"
            )

        response = None

        try:
            response = self.rpc.get_trail(data_rq)
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

        data = TrailParse.get_all(response)

        # Retornar o trail response

        data_rs = GetTrailRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def get_trail_by_date(self, data_rq):
        """
        Retorna uma lista de trilhas, pelo periodo
        de cadastro ou atualização
        """

        if not isinstance(data_rq, GetTrailByDateRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        response = None

        try:
            response = self.rpc.get_trail_by_date(data_rq)

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

        if response['TrailDTOList'] is None:

            return ErrorRS(
                error=True,
                msg='Lista de trilhas é nula ou vazia.'
            )

        data = TrailParse.get_all(
            response,
            response['TrailDTOList']['TrailDTO']
        )

        data_rs = GetTrailByDateRS(
            error=response['hasError'],
            guid=response['Guid'],
            msg=response['Msg'],
            data=data
        )

        return data_rs

    def save(self, data_rq):
        """
        Salva/Atualiza uma trilha
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

    def enroll_student_in_default_discipline(self, data_rq):
        """
        Metodo customizado Matricular o aluno em uma trilha
        """

        if self.customized is False:

            raise ValueError(
                "Esse método é valido somente para ambiente customizado"
            )

        if not isinstance(data_rq, EnrollStudentInDefaultDisciplineRQ):
            raise ValueError(
                "Não existe uma instância para "
                "matricular o aluno em uma disciplina"
            )

        response = None

        try:

            if self.debug:

                self.rpc.debug = self.debug

                response, sent, received = self.rpc.enroll_student_in_default_discipline(
                    data_rq
                )

            else:
                response = self.rpc.enroll_student_in_default_discipline(
                    data_rq
                )

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
                # guid=response['Guid'],
                msg=response['Msg'],
            )

        data_rs = EnrollStudentInDefaultDisciplineRS(
            error=response['hasError'],
            msg=response['Msg']
        )

        if self.debug:

            return data_rs, sent, received

        return data_rs

    def get_all_courses_ordered_by_name(self, data_rq):
        """
        Metodo customizado Retorna todos os Cursos (Grupo de Trilha)
        """

        if self.customized is False:

            raise ValueError(
                "Esse metódo é valido somente para ambiente customizado"
            )

        if not isinstance(data_rq, GetAllCoursesOrderedByNameRQ):
            raise ValueError(
                "Não existe uma instância para a "
                "paginacao dos Grupos de trilha"
            )

        response = None

        try:
            response = self.rpc.get_all_courses_ordered_by_name(data_rq)
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

        data = GroupTrailCustomizedParse.get_all(response)

        # Retornar o group trail response

        data_rs = GetAllCoursesOrderedByNameRS(
            error=response['hasError'],
            msg=response['Msg'],
            data=data
        )

        return data_rs
