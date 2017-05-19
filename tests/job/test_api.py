# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS
)

from lms.job.api import API
from lms.job.containers import *


class JobTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class JobTestCase(JobTestCaseBase):
    """
    Testes para o serviço Cargo
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

    def test_e_instancia_get_all_job_rs(self):
        """
        Testa se a instancia de retorno do metodo get_all é
        GetAllJobRS
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllJobRS)

    def test_sucesso_get_all(self):
        """
        Testa o retorno de sucesso do metodo get_all
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        data = res.data_list

        self.assertEqual(data[0].description, 'Desenvolvimento')

    def test_resposta_error_parametro_job_id_get_job_by_id(self):
        """
        Testa Erro ao passar o parametro lms_job_id como nulo
        """

        data = GetByIdRQ(
            lms_job_id=None
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ExceptionRS):
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

    def test_cargo_nao_encontrado_get_all_job_rs_get_job_by_id(self):
        """
        Testa a resposta de erro caso o cargo nao seja encontrado
        na resposta do metodo get_job_by_id
        """

        data = GetByIdRQ(
            lms_job_id=10000
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(
            res.has_error,
            True
        )

        self.assertEqual(
            res.msg,
            u"Cargo não encontrado"
        )

    def test_e_instancia_get_all_job_rs_get_job_by_id(self):
        """
        Testa se a instancia da resposta do metodo get_job_by_id
        é GetAllJobRS
        """

        data = GetByIdRQ(
            lms_job_id=1
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllJobRS)

    def test_sucesso_get_all_job_rs_get_job_by_id(self):
        """
        Testa o sucesso no retorno do metodo get_job_by_id
        """

        data = GetByIdRQ(
            lms_job_id=1
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(
            res.msg,
            u"Operação realizada com sucesso."
        )

        self.assertFalse(res.has_error)

        job_test = res.data_list[0]

        self.assertEqual(job_test.description, 'Desenvolvimento')

    def test_erro_parametro_save(self):
        """
        Testa erro ao não passar nenhum parametro de cargo no metodo Save
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.save(data)

        self.assertEqual(
            'Não existe uma instância para os dados do cargo',
            excinfo.value.message
        )

    def test_save(self):
        """
        Erro ao salvar um cargo
        """

        data = SaveRQ(
            description=u'Teste job {}'.format(self.fake.name()),
            job_id=self.fake.random_int(min=0, max=99999)
        )

        res = self.api.save(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)
