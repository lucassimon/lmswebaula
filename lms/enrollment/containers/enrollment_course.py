# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lmswebaula.lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class EnrollmentCourseRQ(object):

    _lms_student_id = None

    _lms_class_id = None

    def __init__(self, lms_student_id, lms_class_id):

        self._lms_student_id = lms_student_id
        self._lms_class_id = lms_class_id

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        self._lms_student_id = value

    @property
    def lms_class_id(self):
        return self._lms_class_id

    @lms_class_id.setter
    def lms_class_id(self, value):

        self._lms_class_id = value


class EnrollmentCourseRS(ContainerResponse):

    pass
