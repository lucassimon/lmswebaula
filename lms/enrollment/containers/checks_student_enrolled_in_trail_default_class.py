# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
)


class EnrolledInTrailDefaultClassRQ(object):

    _user_id = 0

    _trail_id = 0

    _lms_trail_id = 0

    def __init__(self, student_id, lms_trail_id=None, trail_id=None):

        if not isinstance(student_id, six.integer_types):
            raise ValueError(
                'O id do estudante precisa ser um inteiro'
            )

        if trail_id:

            if not isinstance(trail_id, six.integer_types):
                raise ValueError(
                    'O id da trilha precisa ser um inteiro'
                )

            self._trail_id = trail_id

        if lms_trail_id:

            if not isinstance(lms_trail_id, six.integer_types):
                raise ValueError(
                    'O id da trilha precisa ser um inteiro'
                )

            self.lms_trail_id = lms_trail_id

        self._user_id = student_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do estudante precisa ser um inteiro'
            )

        self._user_id = value

    @property
    def lms_trail_id(self):
        return self._lms_trail_id

    @lms_trail_id.setter
    def lms_trail_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id da trilha precisa ser um inteiro'
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


class EnrolledInTrailDefaultClassRS(SuccessContainerResponse):

    pass
