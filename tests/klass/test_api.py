# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lmswebaula.lms.klass.api import API
from lmswebaula.lms.klass.containers import *


class KlassTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class KlassTestCase(KlassTestCaseBase):
    """
    Testes para o serviço Class/Turma
    """

    def test_erro_parametro_get_all(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo GetAll
        """

        with pytest.raises(ValueError) as excinfo:

            paginate = {}
            self.api.get_all(paginate)

        self.assertEqual(
            u'Não existe uma instancia para os dados da paginação',
            excinfo.value.message
        )

    def test_e_instancia_get_all_klass_rs(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        self.assertIsInstance(res, GetAllKlassRS)

    def test_busca_turma_pelo_id(self):

        data_rq = GetByIdRQ(
            lms_class_id=10
        )

        res = self.api.get_by_id(data_rq)

        klass_test = res.data_list[0]

        self.assertEqual(klass_test.lms_class_id, 10L)

    def test_sucesso_get_all(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        data = res.data_list

        self.assertEqual(data[0].name, 'TCC')
