# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    ContainerResponse
)


class GetTrailRQ(object):

    _trail_id = None
    _lms_trail_id = None

    def __init__(self, lms_trail_id, trail_id=None):

        self._lms_trail_id = lms_trail_id
        self._trail_id = trail_id

    @property
    def lms_trail_id(self):
        return self._lms_trail_id

    @lms_trail_id.setter
    def lms_trail_id(self, value):

        self._lms_trail_id = value

    @property
    def trail_id(self):
        return self._trail_id

    @trail_id.setter
    def trail_id(self, value):

        self._trail_id = value


class GetTrailRS(ContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Trail&m=GetTrail

    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'As trilhas precisam estar em uma lista'
            )

        self._data_list = data
        self._has_error = error
        self._guid = guid
        self._msg = msg

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):

        if not isinstance(value, list):
            raise ValueError(
                'As trilhas precisam estar em uma lista'
            )

        self._data_list = value
