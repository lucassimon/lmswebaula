# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class StudentEnrolledInTrailDTO(object):

    _state = None

    _ffrom = None

    _to = None

    def __init__(self, state, ffrom, to):

        self._state = state

        self._ffrom = ffrom

        self._to = to

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):

        self._state = value

    @property
    def ffrom(self):
        return self._ffrom

    @ffrom.setter
    def ffrom(self, value):

        self._ffrom = value

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, value):

        self._to = value
