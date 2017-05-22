# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    ContainerResponse
)


class GetByIdRQ(object):

    _teacher_id = None
    _lms_teacher_id = None

    def __init__(self, lms_teacher_id, teacher_id=None):

        self._lms_teacher_id = lms_teacher_id
        self._teacher_id = teacher_id

    @property
    def lms_teacher_id(self):
        return self._lms_teacher_id

    @lms_teacher_id.setter
    def lms_teacher_id(self, value):

        self._lms_teacher_id = value

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):

        self._teacher_id = value
