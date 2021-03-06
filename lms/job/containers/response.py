# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six
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

        if not isinstance(lms_job_id, six.integer_types):
            raise ValueError(
                'O lms id do cargo precisa ser um inteiro'
            )

        self._lms_job_id = lms_job_id
        self._description = description
        self._available = available

        if job_id:

            if not isinstance(job_id, six.integer_types):
                raise ValueError(
                    'O id do cargo precisa ser um inteiro'
                )

            self._job_id = job_id

    @property
    def lms_job_id(self):
        return self._lms_job_id

    @lms_job_id.setter
    def lms_job_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do cargo precisa ser um inteiro'
            )

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

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do cargo precisa ser um inteiro'
            )

        self._job_id = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):

        self._available = value
