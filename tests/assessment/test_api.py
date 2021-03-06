# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS, ExceptionRS, ConnectionExceptionRS
)

from lms.assessment.api import API
from lms.assessment.containers import *


class AssessmentTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = '2ec6aa0a526546c8b3e4f68a78cf68ca'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class AssessmentTestCase(AssessmentTestCaseBase):
    """
    Testes para o serviço Nivel
    """

    def test_erro_parametro_get_delivered_assessment_trail(self):
        """
        Testa erro ao não passar nenhum parametro no metodo
        GetDeliveredAssessmentTrail
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.get_delivered_assessment_trail(data)

        self.assertEqual(
            u'Não existe uma instancia para os dados da busca de nota',
            excinfo.value.message
        )

    def test_e_instancia_get_delivered_assessment_trail_rs(self):
        """
        Testa se a instancia de retorno do metodo
        get_delivered_assessment_trail é GetDeliveredAssessmentTrailRS
        """

        data = GetDeliveredAssessmentTrailRQ(
            lms_trail_class_id=13,
            lms_student_id=7792
        )

        res = self.api.get_delivered_assessment_trail(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        self.assertIsInstance(res, GetDeliveredAssessmentTrailRS)

    def test_sucesso_get_delivered_assessment_trail(self):
        """
        Testa o retorno de sucesso do metodo get_delivered_assessment_trail
        """

        data = GetDeliveredAssessmentTrailRQ(
            page=1,
            page_size=12,
            lms_trail_class_id=11,
            lms_student_id=134
        )

        res = self.api.get_delivered_assessment_trail(data)

        if isinstance(res, ConnectionExceptionRS):
            raise unittest.SkipTest(res.msg)

        data = res.data_list

        self.assertEqual(data[0].name, 'Competência padrão')
