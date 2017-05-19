# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS
)

from lms.enrollment.api import API
from lms.enrollment.containers import *


class EnrollmentTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class EnrollmentTestCase(EnrollmentTestCaseBase):
    """
    Testes para o serviço Student
    """

    def test_erro_parametro_enrollment_course(self):
        """
        Testa erro ao não passar nenhum parametro de Paginação no metodo
        EnrollmentCourse
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.enrollment_course(data)

        self.assertEqual(
            u'Não existe uma instância para os dados da matricula',
            excinfo.value.message
        )

    def test_resposta_error_parametro_student_id_enrollment_course(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=None,
            lms_class_id=None
        )

        res = self.api.enrollment_course(data)

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

    def test_resposta_error_parametro_class_id_enrollment_course(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=15,
            lms_class_id=None
        )

        res = self.api.enrollment_course(data)

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

    def test_e_instancia_enrollment_course_rs_enrollment_course(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=16,
            lms_class_id=10
        )

        res = self.api.enrollment_course(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, EnrollmentCourseRS)

    def test_sucesso_enrollment_course_rs_enrollment_course(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=17,
            lms_class_id=10
        )

        res = self.api.enrollment_course(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)

    def test_erro_parametro_set_status_in_class(self):
        """
        Testa erro ao não passar nenhum parametro de status no metodo
        SetStatusInClass
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.set_status_in_class(data)

        self.assertEqual(
            u'Não existe uma instância para os dados do status',
            excinfo.value.message
        )

    def test_erro_parametro_status_booleano_set_status_in_class_rq_set_status_in_class(self):
        """
        Testa erro ao não passar um parametro status do tipo booleano no
        construtor da classe SetStatusInClassRQ
        """

        with pytest.raises(ValueError) as excinfo:

            data = SetStatusInClassRQ(
                lms_student_id=None,
                lms_class_id=None,
                status=None
            )
            self.api.set_status_in_class(data)

        self.assertEqual(
            u'O status precisa ser um booleano',
            excinfo.value.message
        )

    def test_resposta_error_parametro_student_id_set_status_in_class(self):
        """
        Testa Erro ao setar status do estudante no curso sem os parametros
        lms_sutendent_id
        """

        data = SetStatusInClassRQ(
            lms_student_id=None,
            lms_class_id=None,
            status=True
        )

        res = self.api.set_status_in_class(data)

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

    def test_resposta_error_parametro_class_id_set_status_in_class(self):
        """
        Testa Erro ao setar status do estudante no curso sem os parametros
        lms_class_id
        """

        data = SetStatusInClassRQ(
            lms_student_id=15,
            lms_class_id=None,
            status=True
        )

        res = self.api.set_status_in_class(data)

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

    def test_e_instancia_set_status_in_class_rs_set_status_in_class(self):
        """
        Testa se a instancia da resposta do metodo set_status_in_class
        é SetStatusInClassRS
        """

        data = SetStatusInClassRQ(
            lms_student_id=15,
            lms_class_id=10,
            status=False
        )

        res = self.api.set_status_in_class(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, SetStatusInClassRS)

    def test_sucesso_set_status_in_class_rs_set_status_in_class(self):
        """
        Testa o sucesso na resposta do metodo set_status_in_class
        """

        data = SetStatusInClassRQ(
            lms_student_id=15,
            lms_class_id=10,
            status=False
        )

        res = self.api.set_status_in_class(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, False)
