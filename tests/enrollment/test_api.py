# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from dateutil.relativedelta import relativedelta

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.core.containers.login import LoginRQ
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

    def test_resposta_error_parametro_class_id_enrollment_course(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=15,
            lms_class_id=None
        )

        res = self.api.enrollment_course(data)

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

    def test_e_instancia_enrollment_course_rs_enrollment_course(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrollmentCourseRQ(
            lms_student_id=16,
            lms_class_id=10
        )

        res = self.api.enrollment_course(data)

        if isinstance(res, ConnectionExceptionRS):
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

        if isinstance(res, ConnectionExceptionRS):
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

        if isinstance(res, ConnectionExceptionRS):
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

    def test_erro_checks_student_enrolled_in_trail_class(self):
        """
        Testa erro ao não encontrar matricula para o estudante
        """

        data = EnrolledInTrailClassRQ(
            student_id=15,
            trail_class_id=4
        )

        res = self.api.checks_student_enrolled_in_trail_class(data)

        if isinstance(res, ExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertEqual(res.has_error, True)

        self.assertEqual(res.msg, u'Matricula não encontrada')


class EnrollmentCustomizedTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'c400b95017244830804724aa2c60e000'

        self.api = API(self.passport)

        self.fake = Factory.create('pt_BR')


class EnrollmentCustomizedTestCase(EnrollmentCustomizedTestCaseBase):
    """
    Testes para o serviço Turmas da trilha
    """

    def test_erro_parametro_checks_student_enrolled_in_trail_default_class(
        self
    ):
        """
        Testa erro ao não passar nenhum parametro no metodo
        ChecksStudentEnrolledInTrailDefaultClass
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.checks_student_enrolled_in_trail_default_class(data)

        self.assertEqual(
            u'Não existe uma instância para os dados do aluno matriculado',
            excinfo.value.message
        )

    def test_resposta_error_parametro_student_id_enrolled_in_trail_default_class_rq(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        with pytest.raises(ValueError) as excinfo:

            data = EnrolledInTrailDefaultClassRQ(
                student_id=None,
                trail_id=None
            )
            self.api.checks_student_enrolled_in_trail_default_class(data)

        self.assertEqual(
            u'O id do estudante precisa ser um inteiro',
            excinfo.value.message
        )

    def test_resposta_error_parametro_trail_id_enrolled_in_trail_default_class_rq(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        with pytest.raises(ValueError) as excinfo:

            data = EnrolledInTrailDefaultClassRQ(
                student_id=7790,
                trail_id=None
            )
            self.api.checks_student_enrolled_in_trail_default_class(data)

        self.assertEqual(
            u'O id da trilha precisa ser um inteiro',
            excinfo.value.message
        )

    def test_e_instancia_enrolled_in_trail_default_class_rs_checks_student_enrolled_in_trail_default_class(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrolledInTrailDefaultClassRQ(
            student_id=7790,
            trail_id=9999
        )

        res = self.api.checks_student_enrolled_in_trail_default_class(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, EnrollmentCourseRS)

    def test_matricula_nao_encontrada_checks_student_enrolled_in_trail_default_class(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrolledInTrailDefaultClassRQ(
            student_id=7790,
            trail_id=9999
        )

        res = self.api.checks_student_enrolled_in_trail_default_class(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(res.msg, u'Matricula não encontrada')

    def test_sucesso_checks_student_enrolled_in_trail_default_class(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        data = EnrolledInTrailDefaultClassRQ(
            student_id=7790,
            lms_trail_id=6165
        )

        res = self.api.checks_student_enrolled_in_trail_default_class(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, EnrolledInTrailDefaultClassRS)

        self.assertEqual(res.has_error, False)

    def test_sucesso_get_trails_history_by_class_period(self):
        """
        Testa Erro ao matricular o aluno no curso
        """

        initial_access_date = datetime.date.today() - relativedelta(
            months=+7
        )

        final_access_date = initial_access_date + relativedelta(
            years=+2
        )

        data = GetTrailsHistoryByClassPeriodRQ(
            ffrom=initial_access_date,
            to=final_access_date,
            page=1,
            page_size=1
        )

        res = self.api.checks_student_enrolled_in_trail_default_class(
            data
        )

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetTrailsHistoryByClassPeriodRS)

        self.assertEqual(res.has_error, False)
