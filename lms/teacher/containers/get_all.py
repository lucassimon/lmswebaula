# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    ContainerResponse
)


class GetAllRQ(PaginationMixinRQ):

    pass


class GetAllTeacherRS(ContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Teacher&m=GetAll

    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'Os professores precisam estar em uma lista'
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
                'Os professores precisam estar em uma lista'
            )

        self._data_list = value
