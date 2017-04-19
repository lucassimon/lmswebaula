# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lmswebaula.lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class DataDTO(object):

    _after_term_access = False,
    _apply_access_room = False,
    _automatic = False,
    _calendar_visible = False,
    _class_id = None,
    _class_on_friday = True,
    _class_on_monday = True,
    _class_on_saturday = True,
    _class_on_sunday = True,
    _class_on_thursday = True,
    _class_on_tuesday = True,
    _class_on_wednesday = True,
    _class_room_id = None,
    _course_id = None,
    _date_limit_payment = None,
    _date_registration_limit = None,
    _end_time = None,
    _following_approval_flow = False,
    _free_class = False,
    _hours = None,
    _lms_class_id = "",
    _lms_course_id = "",
    _local_class = None,
    _lote = False,
    _maximum_students = "",
    _name = "",
    _name_menu = "",
    _pre_automatically_enrolls = False,
    _pre_registration = False,
    _pre_registration_validity = False,
    _replica_date = False,
    _replica_pre_registration_date = False,
    _set_severage_class = True,
    _start_time = None,
    _topic_closure_days = "",
    _using_term_course = False

    def __init__(
        self,
        name,
        lms_class_id,
        lms_course_id,
        maximum_students,
        start_time,
        end_time
    ):

        self._name = name
        self._lms_class_id = lms_class_id
        self._lms_course_id = lms_course_id
        self._maximum_students = maximum_students
        self._start_time = start_time
        self._end_time = end_time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def lms_class_id(self):
        return self._lms_class_id

    @lms_class_id.setter
    def lms_class_id(self, value):

        self._lms_class_id = value

    @property
    def lms_course_id(self):
        return self._lms_course_id

    @lms_course_id.setter
    def lms_course_id(self, value):

        self._lms_course_id = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):

        if not isinstance(value, datetime):
            raise ValueError("A data precisa ser um datetime")

        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):

        if not isinstance(value, datetime):
            raise ValueError("A data precisa ser um datetime")

        self._end_time = value

    def convert_to_post(self):
        pass
