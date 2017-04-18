# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

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


class API(object):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Course.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = StudentRPC(
            login=login,
            passport=passport
        )

    def _verifica_exception(self, res, execption_class=Exception):

        if res['hasError']:
            raise execption_class(res['Msg'])

    def get_all(self, paginate_rq):
        """
        Retorna todos os cursos
        """
        pass

    def save(self, student_rq):
        """
        Cria/Atualiza um curso
        """

        pass
