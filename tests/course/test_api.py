# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import ErrorRS, ExceptionRS

from lms.course.api import API
from lms.course.containers import *


class CourseTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class CourseTestCase(CourseTestCaseBase):
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
            u'Não existe uma instancia para os dados da paginação',
            excinfo.value.message
        )

    def test_e_instancia_get_all_course_rs(self):

        paginate = GetAllRQ(page=1, page_size=1)

        res = self.api.get_all(paginate)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllCourseRS)

    def test_sucesso_get_all(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        data = res.data_list

        self.assertEqual(data[0].name, 'TCC')

    def test_resposta_error_parametro_course_id_get_by_id(self):
        """
        Testa Erro ao passar o parametro lms_course_id como nulo
        """

        payload = GetByIdRQ(
            lms_course_id=None
        )

        res = self.api.get_by_id(payload)

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

    def test_curso_nao_encontrado_get_all_course_rs_get_by_id(self):
        """
        Testa a resposta de erro caso o curso nao seja encontrado
        na resposta do metodo get_by_id
        """

        payload = GetByIdRQ(
            lms_course_id=15
        )

        res = self.api.get_by_id(payload)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(
            res.has_error,
            True
        )

        self.assertEqual(
            res.msg,
            u"Curso não encontrado"
        )

    def test_e_instancia_get_all_course_rs_get_by_id(self):
        """
        Testa se a instancia da resposta do metodo get_by_id
        é GetAllCourseRS
        """

        payload = GetByIdRQ(
            lms_course_id=5
        )

        res = self.api.get_by_id(payload)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllCourseRS)

    def test_sucesso_get_all_course_rs_get_by_id(self):
        """
        Testa o sucesso no retorno do metodo get_by_id
        """

        payload = GetByIdRQ(
            lms_course_id=5
        )

        res = self.api.get_by_id(payload)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(
            res.msg,
            u"Operação realizada com sucesso."
        )

        self.assertFalse(res.has_error)

        data = res.data_list[0]

        self.assertEqual(data.name, 'TCC')
