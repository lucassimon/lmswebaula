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
        segment_id=None,
    ):

        if not isinstance(description, six.string_types):
            raise ValueError(
                'A descrição precisa ser uma string'
            )

        self._description = description

        if segment_id is None:
            self._segment_id = segment_id
        else:
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
