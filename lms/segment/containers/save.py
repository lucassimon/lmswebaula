# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


from lmswebaula.lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class SaveRQ(object):

    _lms_segment_id = ''
    _segment_id = ''
    _description = ''

    def __init__(
        self,
        description,
        segment_id,
    ):

        if not isinstance(description, six.string_types):
            raise ValueError(
                'A descrição precisa ser uma string'
            )

        if not isinstance(segment_id, six.integer_types):
            raise ValueError(
                'O segmento_id precisa ser um inteiro'
            )

        self._description = description
        self._segment_id = segment_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'A descrição precisa ser uma string'
            )

        self._description = value

    @property
    def segment_id(self):
        return self._segment_id

    @segment_id.setter
    def segment_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O segmento precisa ser um inteiro'
            )

        self._segment_id = value


class SaveRS(ContainerResponse):
    """
    Resposta do metodo save
    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'Os segmentos precisam estar em uma lista'
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
                'Os segmentos precisam estar em uma lista'
            )

        self._data_list = value
