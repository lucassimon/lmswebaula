# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _student_id = None
    _lms_student_id = None

    def __init__(self, lms_student_id=None, student_id=None):

        if lms_student_id:

            if not isinstance(lms_student_id, six.integer_types):
                raise ValueError(
                    'O lms id do estudante precisa ser um inteiro'
                )

            self._lms_student_id = lms_student_id

        if student_id:

            if not isinstance(student_id, six.integer_types):
                raise ValueError(
                    'O lms id do estudante precisa ser um inteiro'
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
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do estudante precisa ser um inteiro'
            )

        self._student_id = value
