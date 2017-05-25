# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
)


class EnrolledInTrailClassRQ(object):

    _user_id = 0

    _trail_class_id = 0

    def __init__(self, student_id, trail_class_id):

        self._user_id = student_id

        self._trail_class_id = trail_class_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):

        self._user_id = value

    @property
    def trail_class_id(self):
        return self._trail_class_id

    @trail_class_id.setter
    def trail_class_id(self, value):

        self._trail_class_id = value


class EnrolledInTrailClassRS(SuccessContainerResponse):

    pass
