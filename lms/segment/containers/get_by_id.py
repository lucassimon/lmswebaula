# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _segment_id = None
    _lms_segment_id = None

    def __init__(self, lms_segment_id, segment_id=None):

        self._lms_segment_id = lms_segment_id
        self._segment_id = segment_id

    @property
    def lms_segment_id(self):
        return self._lms_segment_id

    @lms_segment_id.setter
    def lms_segment_id(self, value):

        self._lms_segment_id = value

    @property
    def segment_id(self):
        return self._segment_id

    @segment_id.setter
    def segment_id(self, value):

        self._segment_id = value
