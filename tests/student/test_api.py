# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.student.api import API
from lms.student.containers import *


class StudentTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class StudentTestCase(StudentTestCaseBase):
    """
    Testes para o serviço Student
    """

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

    def test_resposta_instancia_get_all_students_rs(self):
        """
        Verifica se a instancia de resposta é um GetAllStudentRS
        """

        paginate = GetAllRQ(page=1, page_size=1)

        res = self.api.get_all(paginate)

        self.assertIsInstance(res, GetAllStudentRS)

    def test_get_all(self):
        """
        Testa se o retorno da resposta veio com sucesso
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        self.assertEqual(res.data_list[0].email, 'webaula@webaula.com.br')

    def test_erro_parametro_set_status(self):
        """
        Testa erro ao não setar um parametro na metodo set_status
        """

        with pytest.raises(ValueError) as excinfo:

            status = {}
            self.api.set_status(status)

        self.assertEqual(
            'Não existe uma instancia para os dados do status',
            excinfo.value.message
        )

    def test_resposta_instancia_status_rs(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        student_test = res.data_list[3]

        status = StatusRQ(
            lms_student_id=int(student_test.lms_student_id),
            active=True
        )

        res = self.api.set_status(status)

        self.assertIsInstance(res, StatusRS)

    def test_set_status_active_false(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        student_test = res.data_list[3]

        status = StatusRQ(
            lms_student_id=int(student_test.lms_student_id),
            active=False
        )

        res = self.api.set_status(status)

        self.assertEqual(res.has_error, False)

        res = self.api.get_all(paginate)

        student_test = res.data_list[3]

        self.assertEqual(student_test.status, False)

    def test_set_status_active_true(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        student_test = res.data_list[3]

        status = StatusRQ(
            lms_student_id=int(student_test.lms_student_id),
            active=True
        )

        res = self.api.set_status(status)

        self.assertEqual(res.has_error, False)

        res = self.api.get_all(paginate)

        student_test = res.data_list[3]

        self.assertEqual(student_test.status, True)

    def test_busca_estudante_pelo_id(self):

        data_rq = GetByIdRQ(
            lms_student_id=15
        )

        res = self.api.get_by_id(data_rq)

        student_test = res.data_list[0]

        self.assertEqual(student_test.status, True)

    def test_erro_parametro_save(self):
        """
        Testa erro ao não passar nenhum parametro de estudante no metodo Save
        """

        with pytest.raises(ValueError) as excinfo:

            student = {}
            self.api.save(student)

        self.assertEqual(
            'Não existe uma instância para os dados do estudante',
            excinfo.value.message
        )

    def test_save(self):
        """
        Erro ao salvar um estudante
        """

        data = SaveRQ(
            name=u'Teste {}'.format(self.fake.name()),
            email=self.fake.email(),
            cpf=self.fake.cpf(),
            password=self.fake.password(
                length=10,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True
            ),
            student_id=self.fake.random_int(min=0, max=9999)
        )

        res = self.api.save(data)

        self.assertEqual(res.has_error, False)
