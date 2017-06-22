# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _class_id = None
    _lms_class_id = None

    def __init__(self, lms_class_id=None, class_id=None):

        if lms_class_id:

            if not isinstance(lms_class_id, six.integer_types):
                raise ValueError(
                    'O lms id da classe precisa ser um inteiro'
                )

            self._lms_class_id = lms_class_id

        if class_id:

            self._class_id = class_id

    @property
    def lms_class_id(self):
        return self._lms_class_id

    @lms_class_id.setter
    def lms_class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do cargo precisa ser um inteiro'
            )

        self._lms_class_id = value

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, value):

        self._class_id = value
