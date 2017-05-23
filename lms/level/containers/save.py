# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
)


class SaveRQ(object):

    _lms_level_id = ''
    _level_id = ''
    _name = ''
    _order = 1

    def __init__(
        self,
        name,
        level_id,
        order,
    ):

        if not isinstance(name, six.string_types):
            raise ValueError(
                'O nome do nivel precisa ser uma string'
            )

        if not isinstance(level_id, six.integer_types):
            raise ValueError(
                'O nivel_id precisa ser um inteiro'
            )

        self._name = name
        self._level_id = level_id
        self._order = order

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'O nome do nivel precisa ser uma string'
            )

        self._name = value

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O nome do nivel precisa ser um inteiro'
            )

        self._order = value

    @property
    def lms_level_id(self):
        return self._lms_level_id

    @lms_level_id.setter
    def lms_level_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O nivel precisa ser um inteiro'
            )

        self._lms_level_id = value

    @property
    def level_id(self):
        return self._level_id

    @level_id.setter
    def level_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O nivel precisa ser um inteiro'
            )

        self._level_id = value


class SaveRS(SuccessContainerResponse):

    pass
