# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _job_id = None
    _lms_job_id = None

    def __init__(self, lms_job_id, job_id=None):

        self._lms_job_id = lms_job_id
        self._job_id = job_id

    @property
    def lms_job_id(self):
        return self._lms_job_id

    @lms_job_id.setter
    def lms_job_id(self, value):

        self._lms_job_id = value

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):

        self._job_id = value
