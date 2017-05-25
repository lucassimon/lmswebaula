# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
)


class EnrollmentCourseRQ(object):

    _lms_student_id = None

    _lms_class_id = None

    _class_id = None

    _student_id = None

    def __init__(
        self,
        lms_student_id=None,
        lms_class_id=None,
        class_id=None,
        student_id=None
    ):

        self._lms_student_id = lms_student_id
        self._lms_class_id = lms_class_id

        self._class_id = class_id
        self._student_id = student_id

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

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        self._student_id = value

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, value):

        self._class_id = value


class EnrollmentCourseRS(SuccessContainerResponse):

    pass
