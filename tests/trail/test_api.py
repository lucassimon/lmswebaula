# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import pytest
import unittest
import datetime
from dateutil.relativedelta import relativedelta

from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.core.containers.login import LoginRQ
from lms.trail.api import API
from lms.trail.containers import *


class TrailTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class TrailTestCase(TrailTestCaseBase):
    """
    Testes para o serviço trilhas

    """
    def test_erro_parametro_get_trail_by_date(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo GetAll
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.get_trail_by_date(data)

        self.assertEqual(
            'Não existe uma instancia para os dados da paginação',
            excinfo.value.message
        )

    def test_erro_parametro_date_begin_get_all_get_trail_by_date(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo GetAll
        """

        with pytest.raises(ValueError) as excinfo:

            data = GetTrailByDateRQ(
                page=1,
                page_size=1,
                date_begin=None,
                date_end=None
            )

            self.api.get_trail_by_date(data)

        self.assertEqual(
            'A data de inicio precisa ser do tipo date',
            excinfo.value.message
        )

    def test_erro_parametro_date_end_get_all_get_trail_by_date(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo GetAll
        """

        now = datetime.date.today()

        with pytest.raises(ValueError) as excinfo:

            data = GetTrailByDateRQ(
                page=1,
                page_size=1,
                date_begin=now,
                date_end=None
            )

            self.api.get_trail_by_date(data)

        self.assertEqual(
            'A data de fim precisa ser do tipo date',
            excinfo.value.message
        )

    def test_resposta_instancia_get_trail_by_date_rs(self):
        """
        Verifica se a instancia de resposta é um get_trail_by_date
        """

        initial_access_date = datetime.date.today() - relativedelta(
            years=+1
        )

        final_access_date = initial_access_date + relativedelta(
            years=+2
        )

        data = GetTrailByDateRQ(
            page=1,
            page_size=1,
            date_begin=initial_access_date,
            date_end=final_access_date
        )

        res = self.api.get_trail_by_date(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetTrailByDateRS)

    def test_get_trail_by_date(self):
        """
        Testa se o retorno da resposta veio com sucesso
        """

        initial_access_date = datetime.date.today() - relativedelta(
            years=+1
        )

        final_access_date = initial_access_date + relativedelta(
            years=+2
        )

        data = GetTrailByDateRQ(
            page=1,
            page_size=1,
            date_begin=initial_access_date,
            date_end=final_access_date
        )

        res = self.api.get_trail_by_date(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.data_list[0].name, u'Padr\xe3o A')


class TrailCustomizedTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'c400b95017244830804724aa2c60e000'

        self.endpoint = 'http://apiandrademartins.webaula.com.br/Trail.svc?singleWsdl'

        self.login = login = LoginRQ(self.passport, url=self.endpoint)

        self.api = API(self.passport, login=login, customized=True)



        self.fake = Factory.create('pt_BR')


class TrailCustomizedTestCase(TrailCustomizedTestCaseBase):
    """
    Testes para o serviço Turmas da trilha
    """

    def test_erro_api_not_customized_get_all_courses_ordered_by_name(self):
        """
        Testa erro ao chamar um metodo de uma api customizada
        """

        self.api = API(self.passport, login=self.login, customized=False)

        with pytest.raises(ValueError) as excinfo:

            data_rq = {}

            self.api.get_all_courses_ordered_by_name(data_rq)

        self.assertEqual(
            u'Esse metódo é valido somente para ambiente customizado',
            excinfo.value.message
        )

    def test_erro_parametro_paginacao_get_all_courses_ordered_by_name(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo
        GetAllCoursesOrderedByName
        """

        with pytest.raises(ValueError) as excinfo:

            paginate = {}
            self.api.get_all_courses_ordered_by_name(paginate)

        self.assertEqual(
            u'Não existe uma instância para a paginacao dos Grupos de trilha',
            excinfo.value.message
        )

    def test_resposta_instancia_get_all_courses_ordered_by_name_rs(self):
        """
        Verifica se a instancia de resposta é um GetAllCoursesOrderedByNameRS
        """

        paginate = GetAllCoursesOrderedByNameRQ(page=1, page_size=1)

        res = self.api.get_all_courses_ordered_by_name(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllCoursesOrderedByNameRS)

    def test_get_all_courses_ordered_by_name(self):
        """
        Testa se o retorno da resposta veio com sucesso
        """

        paginate = GetAllCoursesOrderedByNameRQ(page=1, page_size=1)

        res = self.api.get_all_courses_ordered_by_name(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.data_list[0].name, u' Área de Gestão/MBA')

    def test_erro_api_not_customized_enroll_student_in_default_discipline(
        self
    ):
        """
        Testa erro ao chamar um metodo de uma api customizada
        """

        self.api = API(self.passport, login=self.login, customized=False)

        with pytest.raises(ValueError) as excinfo:

            data_rq = {}

            self.api.enroll_student_in_default_discipline(data_rq)

        self.assertEqual(
            u'Esse método é valido somente para ambiente customizado',
            excinfo.value.message
        )

    def test_erro_parametro_matricular_enroll_student_in_default_discipline(
        self
    ):
        """
        Testa erro ao não passar nenhum parametro de payload no método
        EnrollStudentInDefaultDiscipline
        """

        with pytest.raises(ValueError) as excinfo:

            data_rq = {}
            self.api.enroll_student_in_default_discipline(data_rq)

        self.assertEqual(
            u'Não existe uma instância para matricular o '
            u'aluno em uma disciplina',
            excinfo.value.message
        )

    def test_matricular_aluno_em_disciplina(self):

        initial_access_date = datetime.date.today()

        final_access_date = initial_access_date + relativedelta(
            years=+1
        )

        data = EnrollStudentInDefaultDisciplineRQ(
            lms_student_id=12261,
            discipline_id=4,
            course_id=8,
            initial_access_date=initial_access_date,
            final_access_date=final_access_date
        )

        res = self.api.enroll_student_in_default_discipline(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, EnrollStudentInDefaultDisciplineRS)

        self.assertEqual(res.has_error, False)

    def test_matricular_aluno_em_disciplina_debug_true(self):

        initial_access_date = datetime.date.today()

        final_access_date = initial_access_date + relativedelta(
            years=+1
        )

        data = EnrollStudentInDefaultDisciplineRQ(
            lms_student_id=12261,
            discipline_id=4,
            course_id=8,
            initial_access_date=initial_access_date,
            final_access_date=final_access_date
        )

        self.api.debug = True

        res, sent, received = self.api.enroll_student_in_default_discipline(
            data
        )

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, EnrollStudentInDefaultDisciplineRS)

        self.assertIn(
            '<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">',
            sent
        )

        self.assertIn(
            '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">',
            received
        )

        self.assertEqual(res.has_error, False)

    def test_get_trail_by_date(self):
        """
        Testa se o retorno da resposta veio com sucesso
        """

        self.api = API('c400b95017244830804724aa2c60e000')

        initial_access_date = datetime.date.today() - relativedelta(
            months=+4
        )

        final_access_date = initial_access_date + relativedelta(
            years=+2
        )

        data = GetTrailByDateRQ(
            page=1,
            page_size=1,
            date_begin=initial_access_date,
            date_end=final_access_date
        )

        start_time = time.time()

        res = self.api.get_trail_by_date(data)

        print("--- %s seconds ---" % (time.time() - start_time))

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.data_list[0].name, u'Padr\xe3o A')
