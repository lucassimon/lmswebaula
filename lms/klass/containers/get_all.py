# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import six

from lmswebaula.lms.core.containers.pagination import PaginationMixinRQ
from lmswebaula.lms.core.containers.response import (
    ContainerResponse
)


class GetAllRQ(PaginationMixinRQ):

    pass


class GetAllKlassRS(ContainerResponse):
    """
    Resposta da requisição do get_all
    """

    _data_list = None

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'A classe precisa estar em uma lista'
            )

        self._has_error = error
        self._guid = guid
        self._msg = msg
        self._data_list = data

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):

        self._has_error = value

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):

        self._guid = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):

        self._msg = value

    @property
    def data_list(self):
        return self._data_list
