# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _class_id = None
    _lms_class_id = None

    def __init__(self, lms_class_id, class_id=None):

        self._lms_class_id = lms_class_id
        self._class_id = class_id

    @property
    def lms_class_id(self):
        return self._lms_class_id

    @lms_class_id.setter
    def lms_class_id(self, value):

        self._lms_class_id = value

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, value):

        self._class_id = value
