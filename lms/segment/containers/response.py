# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


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
        self._lms_segment_id = lms_segment_id
        self._description = description

        if segment_id:
            self._segment_id = segment_id

    @property
    def lms_segment_id(self):
        return self._lms_segment_id

    @lms_segment_id.setter
    def lms_segment_id(self, value):

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
