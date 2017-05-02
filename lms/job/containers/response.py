# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class JobDTO(object):

    _lms_job_id = "",
    _job_id = "",
    _description = ""
    _available = False

    def __init__(
        self,
        lms_job_id,
        description,
        job_id=None,
        available=False
    ):
        self._lms_job_id = lms_job_id
        self._description = description
        self._available = available

        if job_id:
            self._job_id = job_id

    @property
    def lms_job_id(self):
        return self._lms_job_id

    @lms_job_id.setter
    def lms_job_id(self, value):

        self._lms_job_id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        self._description = value

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):

        self._job_id = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):

        self._available = value
