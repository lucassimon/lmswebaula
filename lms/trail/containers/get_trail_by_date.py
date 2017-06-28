# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetTrailByDateRQ(PaginationMixinRQ):

    _date_begin = None

    _date_end = None

    def __init__(self, date_begin, date_end, page=1, page_size=12):

        if not isinstance(date_begin, datetime.date):
            raise ValueError(
                'A data de inicio precisa ser do tipo date'
            )

        if not isinstance(date_end, datetime.date):
            raise ValueError(
                'A data de fim precisa ser do tipo date'
            )

        self._page = page
        self._page_size = page_size
        self._date_begin = date_begin
        self._date_end = date_end

    @property
    def date_begin(self):
        return self._date_begin

    @date_begin.setter
    def date_begin(self, value):

        if not isinstance(value, datetime.date):
            raise ValueError(
                'A data de inicio precisa ser do tipo date'
            )

        self._date_begin = value

    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, value):

        if not isinstance(value, datetime.date):
            raise ValueError(
                'A data de fim precisa ser do tipo date'
            )

        self._date_end = value


class GetTrailByDateRS(SuccessContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Trail&m=GetTrailByDate

    """

    pass
