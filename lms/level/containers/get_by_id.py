# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _level_id = None
    _lms_level_id = None

    def __init__(self, lms_level_id=None, level_id=None):

        if lms_level_id:

            if not isinstance(lms_level_id, six.integer_types):
                raise ValueError(
                    'O lms id do nivel precisa ser um inteiro'
                )

            self._lms_level_id = lms_level_id

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
    def level_id(self):
        return self._level_id

    @level_id.setter
    def level_id(self, value):

        self._level_id = value
