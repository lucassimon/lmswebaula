# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _sector_id = None
    _lms_sector_id = None

    def __init__(self, lms_sector_id, sector_id=None):

        self._lms_sector_id = lms_sector_id
        self._sector_id = sector_id

    @property
    def lms_sector_id(self):
        return self._lms_sector_id

    @lms_sector_id.setter
    def lms_sector_id(self, value):

        self._lms_sector_id = value

    @property
    def sector_id(self):
        return self._sector_id

    @sector_id.setter
    def sector_id(self, value):

        self._sector_id = value
