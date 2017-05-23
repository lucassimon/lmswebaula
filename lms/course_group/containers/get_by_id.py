# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _course_group_id = None
    _lms_course_group_id = None

    def __init__(self, lms_course_group_id, course_group_id=None):

        self._lms_course_group_id = lms_course_group_id
        self._course_group_id = course_group_id

    @property
    def lms_course_group_id(self):
        return self._lms_course_group_id

    @lms_course_group_id.setter
    def lms_course_group_id(self, value):

        self._lms_course_group_id = value

    @property
    def course_group_id(self):
        return self._course_group_id

    @course_group_id.setter
    def course_group_id(self, value):

        self._course_group_id = value
