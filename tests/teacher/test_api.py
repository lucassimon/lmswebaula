# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.teacher.api import API
from lms.teacher.containers import *


class TeacherTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class TeacherTestCase(TeacherTestCaseBase):
    """
    Testes para o serviço Teacher
    """

    def test_erro_parametro_save(self):
        """
        Testa erro ao não passar nenhum parametro de professor no metodo Save
        """

        with pytest.raises(ValueError) as excinfo:

            teacher = {}
            self.api.save(teacher)

        self.assertEqual(
            'Não existe uma instância para os dados do professor',
            excinfo.value.message
        )

    def test_save(self):
        """
        Salvar um professor
        """

        data = SaveRQ(
            name=u'Teste {}'.format(
                self.fake.name()
            ),
            email=self.fake.email(),
            cpf=self.fake.cpf(),
            password=self.fake.password(
                length=10,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True
            ),
            status=self.fake.pybool(),
            job=self.fake.job(),
            teacher_id=self.fake.uuid4()

        )

        res = self.api.save(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, SaveRS)

        self.assertEqual(res.has_error, False)

    def test_erro_parametro_get_all(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo GetAll
        """

        with pytest.raises(ValueError) as excinfo:

            paginate = {}
            self.api.get_all(paginate)

        self.assertEqual(
            'Não existe uma instancia para os dados da paginação',
            excinfo.value.message
        )

    def test_resposta_instancia_get_all_teachers_rs(self):
        """
        Verifica se a instancia de resposta é um GetAllTeacherRS
        """

        paginate = GetAllRQ(page=1, page_size=1)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllTeacherRS)

    def test_get_all(self):
        """
        Testa se o retorno da resposta veio com sucesso
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        items = [i for i in res.data_list if i.name == u'Professor Padrão']

        self.assertEqual(items[0].name, 'Professor Padrão')

    def test_resposta_error_parametro_sector_id_get_sector_by_id(self):
        """
        Testa Erro ao passar o parametro lms_sector_id como nulo
        """

        data = GetByIdRQ(
            lms_teacher_id=None
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
                u"Precisamos de um id para pesquisar o professor"
            )
        )

    def test_professor_nao_encontrado_get_all_sector_rs_get_sector_by_id(self):
        """
        Testa a resposta de erro caso o professor nao seja encontrado
        na resposta do metodo get_sector_by_id
        """

        data = GetByIdRQ(
            lms_teacher_id=10000
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
            u"Corpo docente não encontrado"
        )

    def test_e_instancia_get_all_sector_rs_get_sector_by_id(self):
        """
        Testa se a instancia da resposta do metodo get_sector_by_id
        é GetAllTeacherRS
        """

        data = GetByIdRQ(
            lms_teacher_id=7
        )

        res = self.api.get_by_id(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllTeacherRS)

    def test_get_by_id(self):

        data_rq = GetByIdRQ(
            lms_teacher_id=7
        )

        res = self.api.get_by_id(data_rq)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        teacher_test = res.data_list[0]

        self.assertEqual(int(teacher_test.lms_teacher_id), 7)
