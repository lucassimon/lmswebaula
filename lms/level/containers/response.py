# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class LevelDTO(object):

    _lms_level_id = "",
    _level_id = "",
    _name = ""
    _order = 0

    def __init__(
        self,
        lms_level_id,
        name,
        order,
        level_id=None,
    ):

        if lms_level_id:

            if not isinstance(lms_level_id, six.integer_types):
                raise ValueError(
                    'O lms id do nível precisa ser um inteiro'
                )

            self._lms_level_id = lms_level_id

        self._name = name

        self._order = order

        if level_id:

            self._level_id = level_id

    @property
    def lms_level_id(self):
        return self._lms_level_id

    @lms_level_id.setter
    def lms_level_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do nível precisa ser um inteiro'
            )

        self._lms_level_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):

        self._order = value

    @property
    def level_id(self):
        return self._level_id

    @level_id.setter
    def level_id(self, value):

        self._level_id = value
