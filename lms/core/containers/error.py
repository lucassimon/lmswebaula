# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class ErrorRS(ContainerResponse):

    _exception = None

    @property
    def exception(self):
        return self._exception

    @exception.setter
    def exception(self, value):

        self._exception = value
