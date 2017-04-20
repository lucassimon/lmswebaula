# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lmswebaula.lms.core.containers.error import (
    ErrorRS
)

from lmswebaula.lms.enrollment.api import API
from lmswebaula.lms.enrollment.containers import *


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

    def test_resposta_error_parametro_student_id(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=None,
            lms_class_id=None
        )

        res = self.api.enrollment_course(data)

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

    def test_resposta_error_parametro_class_id(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=15L,
            lms_class_id=None
        )

        res = self.api.enrollment_course(data)

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

    def test_e_instancia_enrollment_course_rs(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=15,
            lms_class_id=10
        )

        res = self.api.enrollment_course(data)

        self.assertIsInstance(res, EnrollmentCourseRS)
