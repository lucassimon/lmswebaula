# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lmswebaula.lms.student.api import API
from lmswebaula.lms.student.containers import *


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

    def test_get_all(self):

        paginate = GetAllRQ(page=1, page_size=1)

        students = self.api.get_all(paginate)

        self.assertEqual(students[0].email, 'webaula@webaula.com.br')

    def test_save(self):
        """
        Erro ao salvar um estudante
        """

        data = StudentDTO(
            cpf=self.fake.cpf(),
            email=self.fake.email(),
            login=self.fake.email(),
            name=u'Teste {}'.format(self.fake.name()),
            sex='M',
        )

        result = self.api.save(data)

        self.assertEqual(result, False)
