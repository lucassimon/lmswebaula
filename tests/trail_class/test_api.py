# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.trail_class.api import API
from lms.trail_class.containers import *


class TrailClassTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class TrailClassTestCase(TrailClassTestCaseBase):
    """
    Testes para o serviço Turmas da trilha
    """

    def test_erro_parametro_get(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo Get
        """

        with pytest.raises(ValueError) as excinfo:

            paginate = {}
            self.api.get(paginate)

        self.assertEqual(
            u'Não existe uma instância para os dados da trilha',
            excinfo.value.message
        )

    def test_erro_get(self):
        """
        Testa o retorno de sucesso do metodo get
        """

        paginate = GetRQ(trail_class_id=4)

        res = self.api.get(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, True)

        self.assertEqual(res.msg, u'Turma de trilha n\xe3o encontrada.')
