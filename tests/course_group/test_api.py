# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.course_group.api import API
from lms.course_group.containers import *


class CourseGroupTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class CourseGroupTestCase(CourseGroupTestCaseBase):
    """
    Testes para o serviço grupo de curso
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

    def test_e_instancia_get_all_course_group_rs(self):

        paginate = GetAllRQ(page=1, page_size=1)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllCourseGroupRS)

    def test_sucesso_get_all(self):

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        data = res.data_list

        self.assertEqual(data[0].name, u'Comportamentais')

    def test_resposta_error_parametro_course_group_id_get_by_id(self):
        """
        Testa Erro ao passar o parametro lms_course_id como nulo
        """

        payload = GetByIdRQ(
            lms_course_group_id=None
        )

        res = self.api.get_by_id(payload)

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

    def test_curso_nao_encontrado_get_all_course_group_rs_get_by_id(self):
        """
        Testa a resposta de erro caso o curso nao seja encontrado
        na resposta do metodo get_by_id
        """

        payload = GetByIdRQ(
            lms_course_group_id=15
        )

        res = self.api.get_by_id(payload)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(
            res.has_error,
            True
        )

        self.assertEqual(
            res.msg,
            u"Grupo de curso não encontrado"
        )

    def test_e_instancia_get_all_course_group_rs_get_by_id(self):
        """
        Testa se a instancia da resposta do metodo get_by_id
        é GetAllCourseGroupRS
        """

        payload = GetByIdRQ(
            lms_course_group_id=10121
        )

        res = self.api.get_by_id(payload)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetAllCourseGroupRS)

    def test_sucesso_get_all_course_group_rs_get_by_id(self):
        """
        Testa o sucesso no retorno do metodo get_by_id
        """

        payload = GetByIdRQ(
            lms_course_group_id=10121
        )

        res = self.api.get_by_id(payload)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(
            res.msg,
            u"Operação realizada com sucesso."
        )

        self.assertFalse(res.has_error)

        data = res.data_list[0]

        self.assertEqual(data.name, u'Informática')

    def test_erro_parametro_save(self):
        """
        Testa erro ao não passar nenhum parametro de course no metodo Save
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.save(data)

        self.assertEqual(
            'Não existe uma instância para os dados do curso',
            excinfo.value.message
        )

    def test_save(self):
        """
        Salvar um grupo de curso
        """

        name = u'Teste grupo curso {}'.format(self.fake.name())

        data = SaveRQ(
            name=name,
            highlighted=0,
            course_group_id=self.fake.uuid4()
        )

        res = self.api.save(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)
