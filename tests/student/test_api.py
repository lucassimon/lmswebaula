# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.student.api import API
from lms.student.containers import *


class StudentTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = '2ec6aa0a526546c8b3e4f68a78cf68ca'
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

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllStudentRS)

    def test_get_all(self):
        """
        Testa se o retorno da resposta veio com sucesso
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

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

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[3]

        status = StatusRQ(
            lms_student_id=int(student_test.lms_student_id),
            active=True
        )

        res = self.api.set_status(status)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, StatusRS)

    def test_set_status_active_false(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[3]

        status = StatusRQ(
            lms_student_id=int(student_test.lms_student_id),
            active=False
        )

        res = self.api.set_status(status)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[3]

        self.assertEqual(student_test.status, False)

    def test_set_status_active_true(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[3]

        status = StatusRQ(
            lms_student_id=int(student_test.lms_student_id),
            active=True
        )

        res = self.api.set_status(status)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[3]

        self.assertEqual(student_test.status, True)

    def test_busca_estudante_pelo_id(self):

        data_rq = GetByIdRQ(
            lms_student_id=7792
        )

        res = self.api.get_by_id(data_rq)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[0]

        self.assertEqual(int(student_test.lms_student_id), 15)

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

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)


class StudentCustomizedTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'c400b95017244830804724aa2c60e000'

        self.api = API(self.passport)

        self.fake = Factory.create('pt_BR')


class StudentCustomizedTestCase(StudentCustomizedTestCaseBase):
    """
    Testes para o serviço estudantes de uma api customizada
    """

    def test_get_student_by_id(self):
        """
        Testa erro ao chamar um metodo de uma api customizada
        """

        data_rq = GetByIdRQ(
            lms_student_id=134
        )

        res = self.api.get_by_id(data_rq)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[0]

        self.assertEqual(int(student_test.lms_student_id), 15)

    def test_save_debug(self):
        """
        Erro ao salvar um estudante
        """

        self.api.debug = True

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

        res, sent, received = self.api.save(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIn(
            '<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">',
            sent
        )

        self.assertIn(
            '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">',
            received
        )

        self.assertEqual(res.has_error, True)

    def test_get_student_by_login(self):
        """
        Executa a busca pelo estudante pelo login/cpf
        """

        data_rq = GetByLoginRQ(
            login=14857783100
        )

        res = self.api.get_by_login(data_rq)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        student_test = res.data_list[0]

        self.assertEqual(student_test.email, u'lucassrod@yahooo.com')
