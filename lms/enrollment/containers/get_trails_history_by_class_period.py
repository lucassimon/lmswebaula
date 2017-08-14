# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import six

from lms.core.containers.pagination import PaginationMixinRQ, PaginationMixinRS
from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetTrailsHistoryByClassPeriodRQ(PaginationMixinRQ):
    """
    Paramentro: typeSearch

    Possiveis Valores

    EnrolledInPeriod = Matriculado no periodo

    FinishedOrModifiedInPeriod = Finalizadas ou Modificadas no periodo

    LastAcessInPeriod = Ultimo acesso no periodo

    CompletedInPeriod = Concluidos no periodo
    """

    _ffrom = None

    _to = None

    _type_search = None

    def __init__(
        self,
        ffrom,
        to,
        type_search,
        page=1,
        page_size=12
    ):

        self._page = page
        self._page_size = page_size
        self._ffrom = ffrom
        self._to = to

    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, pagination_rs):

        self._pagination = pagination_rs

    @property
    def ffrom(self):
        return self._ffrom

    @ffrom.setter
    def ffrom(self, value):

        self._ffrom = value

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, value):

        self._to = value

    @property
    def type_search(self):
        return self._type_search

    @type_search.setter
    def type_search(self, value):

        self._type_search = value


class GetTrailsHistoryByClassPeriodRS(SuccessContainerResponse):
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
