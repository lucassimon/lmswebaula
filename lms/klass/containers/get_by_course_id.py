# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByCourseIdRQ(object):

    _course_id = None
    _lms_course_id = None

    def __init__(self, lms_course_id=None, course_id=None):

        if lms_course_id:
            if not isinstance(lms_course_id, six.integer_types):
                raise ValueError(
                    'O lms id do curso precisa ser um inteiro'
                )

            self._lms_course_id = lms_course_id

        if course_id:

            if not isinstance(course_id, six.integer_types):
                raise ValueError(
                    'O id do curso precisa ser um inteiro'
                )

            self._course_id = course_id

    @property
    def lms_course_id(self):
        return self._lms_course_id

    @lms_course_id.setter
    def lms_course_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do curso precisa ser um inteiro'
            )

        self._lms_course_id = value

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do curso precisa ser um inteiro'
            )

        self._course_id = value
