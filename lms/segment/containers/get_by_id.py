# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _segment_id = None
    _lms_segment_id = None

    def __init__(self, lms_segment_id, segment_id=None):

        if not isinstance(lms_segment_id, six.integer_types):
            raise ValueError(
                'O lms id do segmento precisa ser um inteiro'
            )

        self._lms_segment_id = lms_segment_id

        if segment_id:

            if not isinstance(segment_id, six.integer_types):
                raise ValueError(
                    'O id do segmento precisa ser um inteiro'
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
    def segment_id(self):
        return self._segment_id

    @segment_id.setter
    def segment_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do setor precisa ser um inteiro'
            )

        self._segment_id = value
