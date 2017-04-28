# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory

from lms.core.containers.error import (
    ErrorRS
)

from lms.segment.api import API
from lms.segment.containers import *


class SegmentTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.passport = 'adde547e6a7a4ea79741fbee834a07fe'
        self.api = API(self.passport)
        self.fake = Factory.create('pt_BR')


class SegmentTestCase(SegmentTestCaseBase):
    """
    Testes para o serviço Segmento
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

    def test_e_instancia_get_all_segment_rs(self):
        """
        Testa se a instancia de retorno do metodo get_all é
        GetAllSegmentRS
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        self.assertIsInstance(res, GetAllSegmentRS)

    def test_sucesso_get_all(self):
        """
        Testa o retorno de sucesso do metodo get_all
        """

        paginate = GetAllRQ(page=1, page_size=12)

        res = self.api.get_all(paginate)

        data = res.data_list

        self.assertEqual(data[0].description, 'Segmento Padrão')

    def test_resposta_error_parametro_segment_id_get_segment_by_id(self):
        """
        Testa Erro ao passar o parametro lms_segment_id como nulo
        """

        data = GetByIdRQ(
            lms_segment_id=None
        )

        res = self.api.get_by_id(data)

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

    def test_segmento_nao_encontrado_get_all_segment_rs_get_segment_by_id(self):
        """
        Testa a resposta de erro caso o segmento nao seja encontrado
        na resposta do metodo get_segment_by_id
        """

        data = GetByIdRQ(
            lms_segment_id=10000
        )

        res = self.api.get_by_id(data)

        self.assertIsInstance(res, ErrorRS)

        self.assertEqual(
            res.has_error,
            True
        )

        self.assertEqual(
            res.msg,
            u"Segmento não encontrado"
        )

    def test_e_instancia_get_all_segment_rs_get_segment_by_id(self):
        """
        Testa se a instancia da resposta do metodo get_segment_by_id
        é GetAllSegmentRS
        """

        data = GetByIdRQ(
            lms_segment_id=1
        )

        res = self.api.get_by_id(data)

        self.assertIsInstance(res, GetAllSegmentRS)

    def test_sucesso_get_all_segment_rs_get_segment_by_id(self):
        """
        Testa o sucesso no retorno do metodo get_segment_by_id
        """

        data = GetByIdRQ(
            lms_segment_id=1
        )

        res = self.api.get_by_id(data)

        self.assertEqual(
            res.msg,
            u"Operação realizada com sucesso."
        )

        self.assertFalse(res.has_error)

        segment_test = res.data_list[0]

        self.assertEqual(segment_test.description, 'Segmento Padrão')

    def test_resposta_error_parametro_name_get_by_description(self):
        """
        Testa Erro ao passar o parametro lms_segment_id como nulo
        """

        with pytest.raises(ValueError) as excinfo:

            GetByDescriptionRQ(
                description=None
            )

        self.assertEqual(
            u'A descrição precisa ser uma string',
            excinfo.value.message
        )

    def test_segmento_nao_encontrado_get_all_segment_rs_get_by_description(self):
        """
        Testa a resposta de erro caso o segmento nao seja encontrado
        na resposta do metodo get_segment_by_id
        """

        data = GetByDescriptionRQ(
            description='Segmento 1'
        )

        res = self.api.get_by_description(data)

        self.assertEqual(
            res.has_error,
            False
        )

        self.assertEqual(
            len(res.data_list),
            0
        )

    def test_e_instancia_get_all_segment_rs_get_by_description(self):
        """
        Testa se a instancia da resposta do metodo get_segment_by_id
        é GetAllSegmentRS
        """

        data = GetByDescriptionRQ(
            description='Segmento Padrão'
        )

        res = self.api.get_by_description(data)

        self.assertIsInstance(res, GetAllSegmentRS)

    def test_sucesso_get_all_segment_rs_get_by_description(self):
        """
        Testa o sucesso no retorno do metodo get_segment_by_id
        """

        data = GetByDescriptionRQ(
            description='Segmento Padrão'
        )

        res = self.api.get_by_description(data)

        self.assertEqual(
            res.msg,
            u"Operação realizada com sucesso."
        )

        self.assertFalse(res.has_error)

        segment_test = res.data_list[0]

        self.assertEqual(segment_test.description, 'Segmento Padrão')

    def test_erro_parametro_save(self):
        """
        Testa erro ao não passar nenhum parametro de segmento no metodo Save
        """

        with pytest.raises(ValueError) as excinfo:

            data = {}
            self.api.save(data)

        self.assertEqual(
            'Não existe uma instância para os dados do segmento',
            excinfo.value.message
        )

    def test_save(self):
        """
        Erro ao salvar um segmento
        """

        data = SaveRQ(
            description=u'Teste segmento {}'.format(self.fake.name()),
            segment_id=self.fake.random_int(min=0, max=99999)
        )

        res = self.api.save(data)

        self.assertEqual(res.has_error, False)
