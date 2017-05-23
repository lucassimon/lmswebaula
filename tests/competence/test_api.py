# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.competence.api import API
from lms.competence.containers import *


class CompetenceTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class CompetenceTestCase(CompetenceTestCaseBase):
    """
    Testes para o serviço Nivel
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

    def test_e_instancia_get_all_competence_rs(self):
        """
        Testa se a instancia de retorno do metodo get_all é
        GetAllCompetenceRS
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllCompetenceRS)

    def test_sucesso_get_all(self):
        """
        Testa o retorno de sucesso do metodo get_all
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        data = res.data_list

        self.assertEqual(data[0].name, 'Competência padrão')

    def test_resposta_error_parametro_competence_id_get_competence_by_id(self):
        """
        Testa Erro ao passar o parametro lms_competence_id como nulo
        """

        data = GetByIdRQ(
            lms_competence_id=None
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

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

    def test_setor_nao_encontrado_get_all_competence_rs_get_competence_by_id(
        self
    ):
        """
        Testa a resposta de erro caso o setor nao seja encontrado
        na resposta do metodo get_competence_by_id
        """

        data = GetByIdRQ(
            lms_competence_id=10000
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(
            res.has_error,
            True
        )

        self.assertEqual(
            res.msg,
            u"Competencia não encontrada"
        )

    def test_e_instancia_get_all_competence_rs_get_competence_by_id(self):
        """
        Testa se a instancia da resposta do metodo get_competence_by_id
        é GetAllCompetenceRS
        """

        data = GetByIdRQ(
            lms_competence_id=1
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllCompetenceRS)

    def test_sucesso_get_all_competence_rs_get_competence_by_id(self):
        """
        Testa o sucesso no retorno do metodo get_competence_by_id
        """

        data = GetByIdRQ(
            lms_competence_id=1
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(
            res.msg,
            u"Operação realizada com sucesso."
        )

        self.assertFalse(res.has_error)

        competence_test = res.data_list[0]

        self.assertEqual(competence_test.name, 'Competência padrão')

    def test_erro_parametro_save(self):
        """
        Testa erro ao não passar nenhum parametro de setor no metodo Save
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.save(data)

        self.assertEqual(
            'Não existe uma instância para os dados do setor',
            excinfo.value.message
        )

    def test_save(self):
        """
        Erro ao salvar um setor
        """

        data = SaveRQ(
            name=u'Teste competence {}'.format(self.fake.name()),
            competence_id=self.fake.random_int(min=0, max=99999),
        )

        res = self.api.save(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)
