# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lmswebaula.lms.core.containers.error import (
    ErrorRS
)

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
        """
        Testa se a instancia de retorno do metodo get_all é
        GetAllKlassRS
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        self.assertIsInstance(res, GetAllKlassRS)

    def test_sucesso_get_all(self):
        """
        Testa o retorno de sucesso do metodo get_all
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        data = res.data_list

        self.assertEqual(data[0].name, 'TCC')

    def test_busca_turma_pelo_id(self):
        """
        Testa o retorno do metodo GetById que busca os dados da turma
        """
        data_rq = GetByIdRQ(
            lms_class_id=10
        )

        res = self.api.get_by_id(data_rq)

        klass_test = res.data_list[0]

        self.assertEqual(klass_test.lms_class_id, 10L)

    def test_resposta_error_parametro_course_id_get_course_by_id(self):
        """
        Testa Erro ao passar o parametro lms_course_id como nulo
        """

        data = GetByCourseIdRQ(
            lms_course_id=None
        )

        res = self.api.get_by_course_id(data)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(
            res.has_error,
            True
        )

        self.assertEqual(
            res.msg,
            (
                u"Deve ser informado a chave do registro "
                u"no sistema legado ou do LMS."
            )
        )

    def test_curso_nao_encontrado_get_all_klass_rs_get_course_by_id(self):
        """
        Testa a resposta de erro caso o curso nao seja encontrado
        na resposta do metodo get_course_by_id
        """

        data = GetByCourseIdRQ(
            lms_course_id=15
        )

        res = self.api.get_by_course_id(data)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(
            res.has_error,
            True
        )

        self.assertEqual(
            res.msg,
            u"Curso não encontrado"
        )

    def test_e_instancia_get_all_klass_rs_get_course_by_id(self):
        """
        Testa se a instancia da resposta do metodo get_course_by_id
        é GetAllKlassRS
        """

        data = GetByCourseIdRQ(
            lms_course_id=5
        )

        res = self.api.get_by_course_id(data)

        self.assertIsInstance(res, GetAllKlassRS)

    def test_sucesso_get_all_klass_rs_get_course_by_id(self):
        """
        Testa o sucesso no retorno do metodo get_course_by_id
        """

        data = GetByCourseIdRQ(
            lms_course_id=5
        )

        res = self.api.get_by_course_id(data)

        self.assertEqual(
            res.msg,
            u"Operação realizada com sucesso."
        )

        self.assertFalse(res.has_error)

        klass_test = res.data_list[0]

        self.assertEqual(klass_test.name, 'TCC')
