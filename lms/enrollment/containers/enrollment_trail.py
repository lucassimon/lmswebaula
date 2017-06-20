# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
)


class EnrollmentTrailRQ(object):

    _lms_student_id = None

    _student_id = None

    _lms_trail_class_id = None

    _enrolled = None

    def __init__(
        self,
        lms_student_id=None,
        lms_class_id=None,
        class_id=None,
        student_id=None
    ):
        if lms_student_id:

            if not isinstance(lms_student_id, six.integer_types):
                raise ValueError(
                    'O lms id do estudante precisa ser um inteiro'
                )

            self._lms_student_id = lms_student_id

        if lms_class_id:

            if not isinstance(lms_class_id, six.integer_types):
                raise ValueError(
                    'O lms id da classe precisa ser um inteiro'
                )

            self._lms_class_id = lms_class_id

        if class_id:

            if not isinstance(class_id, six.integer_types):
                raise ValueError(
                    'O id da classe precisa ser um inteiro'
                )

            self._class_id = class_id

        if student_id:

            if not isinstance(student_id, six.integer_types):
                raise ValueError(
                    'O id do estudante precisa ser um inteiro'
                )

            self._student_id = student_id

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do estudante precisa ser um inteiro'
            )

        self._lms_student_id = value

    @property
    def lms_class_id(self):
        return self._lms_class_id

    @lms_class_id.setter
    def lms_class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da classe precisa ser um inteiro'
            )

        self._lms_class_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do estudante precisa ser um inteiro'
            )

        self._student_id = value

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id da classe precisa ser um inteiro'
            )

        self._class_id = value


class EnrollmentCourseRS(SuccessContainerResponse):

    pass
