# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class SaveRQ(object):

    _lms_sector_id = ''
    _sector_id = ''
    _name = ''

    def __init__(
        self,
        name,
        sector_id,
        available=False
    ):

        if not isinstance(name, six.string_types):
            raise ValueError(
                'O nome do departamento precisa ser uma string'
            )

        if not isinstance(sector_id, six.integer_types):
            raise ValueError(
                'O departamento_id precisa ser um inteiro'
            )

        self._name = name
        self._sector_id = sector_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'O nome do departamento precisa ser uma string'
            )

        self._name = value

    @property
    def lms_sector_id(self):
        return self._lms_sector_id

    @lms_sector_id.setter
    def lms_sector_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O departamento precisa ser um inteiro'
            )

        self._lms_sector_id = value

    @property
    def sector_id(self):
        return self._sector_id

    @sector_id.setter
    def sector_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O departamento precisa ser um inteiro'
            )

        self._sector_id = value


class SaveRS(ContainerResponse):
    """
    Resposta do metodo save
    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'Os departamentos precisam estar em uma lista'
            )

        self._data_list = data
        self._has_error = error
        self._guid = guid
        self._msg = msg

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):

        if not isinstance(value, list):
            raise ValueError(
                'Os departamentos precisam estar em uma lista'
            )

        self._data_list = value
