# -*- coding: utf-8 -*-


from __future__ import unicode_literals

import six

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class NoteReviewDTO(object):

    _name = ""
    _number_of_issues = 0
    _mastery_score = 0
    _value = 0
    _corelesson_status = ""
    _core_score_raw = 0
    _score = 0
    _date_last_access = None
    _lms_evaluation_id = 0
    _evaluation_id = 0
    _lms_student_id = 0
    _student_id = 0

    def __init__(
        self,
        name,
        mastery_score,
        value,
        score,
        lms_evaluation_id,
        lms_student_id
    ):

        if not isinstance(lms_student_id, six.integer_types):
            raise ValueError(
                'O lms id do estudante precisa ser um inteiro'
            )

        self._lms_student_id = lms_student_id

        if not isinstance(lms_evaluation_id, six.integer_types):
            raise ValueError(
                'O lms id da avaliação precisa ser um inteiro'
            )

        self._lms_evaluation_id = lms_evaluation_id

        self._name = name

        self._mastery_score = mastery_score

        self._value = value

        self._score = score

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
    def lms_evaluation_id(self):
        return self._lms_evaluation_id

    @lms_evaluation_id.setter
    def lms_evaluation_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da avaliação precisa ser um inteiro'
            )

        self._lms_evaluation_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'O lms id do estudante precisa ser um inteiro'
            )

        self._name = value

    @property
    def number_of_issues(self):
        return self._number_of_issues

    @number_of_issues.setter
    def number_of_issues(self, value):

        self._number_of_issues = value

    @property
    def mastery_score(self):
        return self._mastery_score

    @mastery_score.setter
    def mastery_score(self, value):

        self._mastery_score = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):

        self._value = value

    @property
    def corelesson_status(self):
        return self._corelesson_status

    @corelesson_status.setter
    def corelesson_status(self, value):

        self._corelesson_status = value

    @property
    def core_score_raw(self):
        return self._core_score_raw

    @core_score_raw.setter
    def core_score_raw(self, value):

        self._core_score_raw = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):

        self._score = value

    @property
    def date_last_access(self):
        return self._date_last_access

    @date_last_access.setter
    def date_last_access(self, value):

        self._date_last_access = value

    @property
    def evaluation_id(self):
        return self._evaluation_id

    @evaluation_id.setter
    def evaluation_id(self, value):

        self._evaluation_id = value

    @property
    def student_id(self):
        return self._evaluation_id

    @student_id.setter
    def student_id(self, value):

        self._student_id = value
