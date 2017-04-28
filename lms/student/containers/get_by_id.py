# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    ContainerResponse
)


class GetByIdRQ(object):

    _student_id = None
    _lms_student_id = None

    def __init__(self, lms_student_id, student_id=None):

        self._lms_student_id = lms_student_id
        self._student_id = student_id

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        self._lms_student_id = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):

        self._student_id = value

