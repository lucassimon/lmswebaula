# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _course_id = None
    _lms_course_id = None

    def __init__(self, lms_course_id, course_id=None):

        self._lms_course_id = lms_course_id
        self._course_id = course_id

    @property
    def lms_course_id(self):
        return self._lms_course_id

    @lms_course_id.setter
    def lms_course_id(self, value):

        self._lms_course_id = value

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):

        self._course_id = value