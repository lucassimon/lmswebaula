# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six
import datetime

from lms.core.containers.response import (
    SuccessContainerResponse
)


class EnrollStudentInDefaultDisciplineRQ(object):

    _lms_student_id = 0
    _student_id = 0
    _discipline_id = 0
    _course_id = 0
    _initial_access_date = None
    _final_access_date = None

    def __init__(
        self,
        lms_student_id,
        discipline_id,
        course_id,
        initial_access_date,
        final_access_date,
        student_id=None
    ):

        if not isinstance(lms_student_id, six.integer_types):
            raise ValueError(
                'O lms id do estudante precisa ser um inteiro'
            )

        if not isinstance(initial_access_date, datetime.date):
            raise ValueError(
                'A data inicial de acesso do estudante precisa '
                'ser do tipo date'
            )

        if not isinstance(final_access_date, datetime.date):
            raise ValueError(
                'A data final de acesso do estudante precisa '
                'ser do tipo date'
            )

        self._lms_student_id = lms_student_id

        if student_id:

            self._student_id = student_id

        self._discipline_id = discipline_id

        self._course_id = course_id

        self._initial_access_date = initial_access_date

        self._final_access_date = final_access_date

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
    def discipline_id(self):
        return self._discipline_id

    @discipline_id.setter
    def discipline_id(self, value):

        self._discipline_id = value

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):

        self._course_id = value

    @property
    def initial_access_date(self):
        return self._initial_access_date

    @initial_access_date.setter
    def initial_access_date(self, value):

        if not isinstance(value, datetime.date):
            raise ValueError(
                'A data inicial de acesso do estudante precisa '
                'ser do tipo date'
            )

        self._initial_access_date = value

    @property
    def final_access_date(self):
        return self._final_access_date

    @final_access_date.setter
    def final_access_date(self, value):

        if not isinstance(value, datetime.date):
            raise ValueError(
                'A data final de acesso do estudante precisa '
                'ser do tipo date'
            )

        self._final_access_date = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        self._student_id = value


class EnrollStudentInDefaultDisciplineRS(SuccessContainerResponse):

    pass
