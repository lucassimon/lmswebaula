# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import six

from lms.core.containers.pagination import PaginationMixinRQ, PaginationMixinRS
from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetAllRQ(PaginationMixinRQ):

    pass


class GetAllCourseRS(SuccessContainerResponse):
    """
    Resposta da requisição do get_all
    """

    _pagination = None

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination_rs):

        self._pagination = pagination_rs
