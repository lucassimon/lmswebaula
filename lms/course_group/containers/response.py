# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class CourseGroupDTO(object):

    _lms_course_group_id = 0
    _course_group_id = None
    _name = ''
    _highlighted = 0

    def __init__(
        self,
        lms_course_group_id,
        highlighted,
        name,
        course_group_id=None
    ):
        self._lms_course_group_id = lms_course_group_id

        if course_group_id:
            self._course_group_id = course_group_id

        self._highlighted = highlighted

        self._name = name

    @property
    def lms_course_group_id(self):
        return self._lms_course_group_id

    @lms_course_group_id.setter
    def lms_course_group_id(self, value):

        self._lms_course_group_id = value

    @property
    def course_group_id(self):
        return self._course_group_id

    @course_group_id.setter
    def course_group_id(self, value):

        self._course_group_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def highlighted(self):
        return self._highlighted

    @highlighted.setter
    def highlighted(self, value):

        self._highlighted = value
