# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _course_group_id = None
    _lms_course_group_id = None

    def __init__(self, lms_course_group_id, course_group_id=None):

        if lms_course_group_id:

            if not isinstance(lms_course_group_id, six.integer_types):
                raise ValueError(
                    'O lms id da curso de grupo precisa ser um inteiro'
                )

            self._lms_course_group_id = lms_course_group_id

        if course_group_id:

            self._course_group_id = course_group_id

    @property
    def lms_course_group_id(self):
        return self._lms_course_group_id

    @lms_course_group_id.setter
    def lms_course_group_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do grupo de curso precisa ser um inteiro'
            )

        self._lms_course_group_id = value

    @property
    def course_group_id(self):
        return self._course_group_id

    @course_group_id.setter
    def course_group_id(self, value):

        self._course_group_id = value
