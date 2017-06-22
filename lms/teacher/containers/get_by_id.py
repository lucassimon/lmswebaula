# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _teacher_id = None
    _lms_teacher_id = None

    def __init__(self, lms_teacher_id=None, teacher_id=None):

        if lms_teacher_id:
            if not isinstance(lms_teacher_id, six.integer_types):
                raise ValueError(
                    'O lms id do professor precisa ser um inteiro'
                )

            self._lms_teacher_id = lms_teacher_id

        if teacher_id:

            self._teacher_id = teacher_id

    @property
    def lms_teacher_id(self):
        return self._lms_teacher_id

    @lms_teacher_id.setter
    def lms_teacher_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do professor precisa ser um inteiro'
            )

        self._lms_teacher_id = value

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):

        self._teacher_id = value
