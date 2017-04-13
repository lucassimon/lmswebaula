# -*- coding: utf-8 -*-
import unittest

from datetime import datetime
from lmswebaula.student.api import API


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        print "Inicio do teste"

    def test_get_all(self):
        """
        Teste para buscar todos os estudantes
        """
        api = API(passport='123')

        api.get_all()

        self.assertTrue(True, True)


if __name__ == '__main__':
    unittest.main()
