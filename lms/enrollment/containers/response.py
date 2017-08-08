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

    def __init__(
        self,
        lms_student_id,
        lms_trail_id,
        lms_trail_class_id,
        percent_utilization,
        percent_conclusion,
        finalized
    ):

        self._lms_student_id = lms_student_id

        self._lms_trail_id = lms_trail_id

        self._lms_trail_class_id = lms_trail_class_id

        self._percent_utilization = percent_utilization

        self._percent_conclusion = percent_conclusion

        self._finalized = finalized

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

    @property
    def trail_id(self):
        return self._trail_id

    @trail_id.setter
    def trail_id(self, value):

        self._trail_id = value

    @property
    def lms_trail_class_id(self):
        return self._lms_trail_class_id

    @lms_trail_class_id.setter
    def lms_trail_class_id(self, value):

        self._lms_trail_class_id = value

    @property
    def percent_utilization(self):
        return self._percent_utilization

    @percent_utilization.setter
    def percent_utilization(self, value):

        self._percent_utilization = value

    @property
    def percent_conclusion(self):
        return self._percent_conclusion

    @percent_conclusion.setter
    def percent_conclusion(self, value):

        self._percent_conclusion = value

    @property
    def concluded_on(self):
        return self._concluded_on

    @concluded_on.setter
    def concluded_on(self, value):

        self._concluded_on = value

    @property
    def accessed_on(self):
        return self._accessed_on

    @accessed_on.setter
    def accessed_on(self, value):

        self._accessed_on = value

    @property
    def first_access(self):
        return self._first_access

    @first_access.setter
    def first_access(self, value):

        self._first_access = value

    @property
    def finalized(self):
        return self._finalized

    @finalized.setter
    def finalized(self, value):

        self._finalized = value

    @property
    def registration_date(self):
        return self._registration_date

    @registration_date.setter
    def registration_date(self, value):

        self._registration_date = value

    @property
    def trail_class_date_begin(self):
        return self._trail_class_date_begin

    @trail_class_date_begin.setter
    def trail_class_date_begin(self, value):

        self._trail_class_date_begin = value

    @property
    def trail_class_date_end(self):
        return self._trail_class_date_end

    @trail_class_date_end.setter
    def trail_class_date_end(self, value):

        self._trail_class_date_end = value

    @property
    def date_modification(self):
        return self._date_modification

    @date_modification.setter
    def date_modification(self, value):

        self._date_modification = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        self._status = value
