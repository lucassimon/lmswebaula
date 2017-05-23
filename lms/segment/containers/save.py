# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
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
    def lms_segment_id(self):
        return self._lms_segment_id

    @lms_segment_id.setter
    def lms_segment_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O segment precisa ser um inteiro'
            )

        self._lms_segment_id = value

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


class SaveRS(SuccessContainerResponse):

    pass
