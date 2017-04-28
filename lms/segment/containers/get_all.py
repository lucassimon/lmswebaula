# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import six

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    ContainerResponse
)


class GetAllRQ(PaginationMixinRQ):

    pass


class GetAllSegmentRS(ContainerResponse):
    """
    Resposta da requisição do get_all
    """

    _data_list = None

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'O segmento precisa estar em uma lista'
            )

        self._has_error = error
        self._guid = guid
        self._msg = msg
        self._data_list = data

    @property
    def data_list(self):
        return self._data_list
