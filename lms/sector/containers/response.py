# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class SectorDTO(object):

    _lms_sector_id = "",
    _sector_id = "",
    _name = ""
    _available = False

    def __init__(
        self,
        lms_sector_id,
        name,
        sector_id=None,
    ):

        if not isinstance(lms_sector_id, six.integer_types):
            raise ValueError(
                'O lms id do setor precisa ser um inteiro'
            )

        self._lms_sector_id = lms_sector_id
        self._name = name

        if sector_id:

            if not isinstance(lms_sector_id, six.integer_types):
                raise ValueError(
                    'O id do setor precisa ser um inteiro'
                )

            self._sector_id = sector_id

    @property
    def lms_sector_id(self):
        return self._lms_sector_id

    @lms_sector_id.setter
    def lms_sector_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do setor precisa ser um inteiro'
            )

        self._lms_sector_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def sector_id(self):
        return self._sector_id

    @sector_id.setter
    def sector_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do setor precisa ser um inteiro'
            )

        self._sector_id = value
