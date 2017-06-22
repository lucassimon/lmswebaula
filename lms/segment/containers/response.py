# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class SegmentDTO(object):

    _lms_segment_id = "",
    _segment_id = "",
    _description = ""

    def __init__(
        self,
        lms_segment_id,
        description,
        segment_id=None
    ):

        if lms_segment_id:

            if not isinstance(lms_segment_id, six.integer_types):
                raise ValueError(
                    'O lms id do segmento precisa ser um inteiro'
                )

            self._lms_segment_id = lms_segment_id

        self._description = description

        if segment_id:

            if not isinstance(segment_id, six.integer_types):
                raise ValueError(
                    'O lms id do setor precisa ser um inteiro'
                )

            self._segment_id = segment_id

    @property
    def lms_segment_id(self):
        return self._lms_segment_id

    @lms_segment_id.setter
    def lms_segment_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do segmento precisa ser um inteiro'
            )

        self._lms_segment_id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        self._description = value

    @property
    def segment_id(self):
        return self._segment_id

    @segment_id.setter
    def segment_id(self, value):

        self._segment_id = value
