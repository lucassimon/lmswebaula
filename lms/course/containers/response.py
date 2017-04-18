# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lmswebaula.lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class CourseRS(ContainerResponse):
    """

    """

    _course_list = []

    def __init__(self, error=True, guid='', msg='', courses=[]):

        self._has_error = error
        self._guid = guid
        self._msg = msg
        self._course_list = courses

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):

        self._has_error = value

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):

        self._guid = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):

        self._msg = value

    @property
    def _course_list(self):
        return self.__course_list

    @_course_list.setter
    def _course_list(self, value):

        if not isinstance(value, list):
            raise ValueError(
                'O curso precisa estar em uma lista'
            )

        self._course_list = value
