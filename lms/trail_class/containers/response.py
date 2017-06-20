# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class TrailClassDTO(object):

    _lms_trail_class_id = 0
    _trail_class_id = None
    _lms_trail_id = 0
    _trail_id = None
    _name = ''
    _description = ''
    _vacancies = None
    _is_vacancies_unlimited = None
    _from = None
    _to = None
    _time_from = ''
    _time_to = ''
    _is_always_available = None
    _students = []

    def __init__(
        self,
        lms_trail_id,
        trail_id,
        lms_trail_class_id,
        trail_class_id,
        name,
        description,
        time_from,
        time_to,
        students
    ):
        if not isinstance(lms_trail_id, six.integer_types):
            raise ValueError(
                'O lms id da trilha precisa ser um inteiro'
            )

        self._lms_trail_id = lms_trail_id

        if trail_id:

            if not isinstance(trail_id, six.integer_types):
                raise ValueError(
                    'O id da trilha precisa ser um inteiro'
                )

            self._trail_id = trail_id

        self._lms_trail_class_id = lms_trail_class_id

        if not isinstance(lms_trail_class_id, six.integer_types):
            raise ValueError(
                'O lms id da classe da trilha precisa ser um inteiro'
            )

        if trail_class_id:

            if not isinstance(trail_class_id, six.integer_types):
                raise ValueError(
                    'O id da classe da trilha precisa ser um inteiro'
                )

            self._trail_class_id = trail_class_id

        self._name = name

        self._description = description

        self._time_from = time_from

        self._time_to = time_to

        self._students = students

    @property
    def lms_trail_id(self):
        return self._lms_trail_id

    @lms_trail_id.setter
    def lms_trail_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da trilha precisa ser um inteiro'
            )
        self._lms_trail_id = value

    @property
    def trail_id(self):
        return self._trail_id

    @trail_id.setter
    def trail_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id da trilha precisa ser um inteiro'
            )

        self._trail_id = value

    @property
    def lms_trail_class_id(self):
        return self._lms_trail_id

    @lms_trail_class_id.setter
    def lms_trail_class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da classe da trilha precisa ser um inteiro'
            )

        self._lms_trail_class_id = value

    @property
    def trail_class_id(self):
        return self._trail_class_id

    @trail_class_id.setter
    def trail_class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da trilha precisa ser um inteiro'
            )

        self._trail_class_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        self._description = value

    @property
    def time_from(self):
        return self._time_from

    @time_from.setter
    def time_from(self, value):

        self._time_from = value

    @property
    def time_to(self):
        return self._time_to

    @time_to.setter
    def time_to(self, value):

        self._time_to = value

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, value):

        self._students = value


class StudentTrailClass(object):

    _lms_student_id = 0
    _student_id = None
    _name = ''
    _state = ''

    def __init__(
        self,
        lms_student_id,
        name,
        state,
        student_id=None
    ):

        if not isinstance(lms_student_id, six.integer_types):
            raise ValueError(
                'O lms id do estudante precisa ser um inteiro'
            )

        self._lms_student_id = lms_student_id

        if student_id:

            if not isinstance(student_id, six.integer_types):
                raise ValueError(
                    'O lms id da trilha precisa ser um inteiro'
                )

            self._student_id = student_id

        self._name = name

        self._state = state

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da trilha precisa ser um inteiro'
            )

        self._lms_student_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da trilha precisa ser um inteiro'
            )

        self._student_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):

        self._state = value
