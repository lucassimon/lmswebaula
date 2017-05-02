# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _level_id = None
    _lms_level_id = None

    def __init__(self, lms_level_id, level_id=None):

        self._lms_level_id = lms_level_id
        self._level_id = level_id

    @property
    def lms_level_id(self):
        return self._lms_level_id

    @lms_level_id.setter
    def lms_level_id(self, value):

        self._lms_level_id = value

    @property
    def level_id(self):
        return self._level_id

    @level_id.setter
    def level_id(self, value):

        self._level_id = value
