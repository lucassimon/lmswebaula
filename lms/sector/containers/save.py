# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse
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


class SaveRS(SuccessContainerResponse):

    pass
