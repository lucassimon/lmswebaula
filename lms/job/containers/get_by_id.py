# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _job_id = None
    _lms_job_id = None

    def __init__(self, lms_job_id, job_id=None):

        if not isinstance(lms_job_id, six.integer_types):
            raise ValueError(
                'O lms id do cargo precisa ser um inteiro'
            )

        self._lms_job_id = lms_job_id

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
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id do cargo precisa ser um inteiro'
            )

        self._job_id = value
