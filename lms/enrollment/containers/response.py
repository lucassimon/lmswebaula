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


class StudentTrailSituationDTO(object):

    _lms_student_id = None

    _student_id = None

    _lms_trail_id = None

    _trail_id = None

    _lms_trail_class_id = None

    _trail_class_id = None

    _percent_utilization = None

    _percent_conclusion = None

    _concluded_on = None

    _accessed_on = None

    _first_access = None

    _finalized = False

    _registration_date = None

    _trail_class_date_begin = None

    _trail_class_date_end = None

    _date_modification = None

    _status = None

    def __init__(self, lms_student_id, ffrom, to):

        self._lms_student_id = lms_student_id

        self._ffrom = ffrom

        self._to = to

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        self._lms_student_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        self._student_id = value

    @property
    def lms_trail_id(self):
        return self._lms_trail_id

    @lms_trail_id.setter
    def lms_trail_id(self, value):

        self._lms_trail_id = value