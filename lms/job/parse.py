# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.job.containers import *


class JobParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['JobListDTO']['JobDTO']
        except Exception:
            return data

        for std in ws_data:

            dt = JobDTO(
                lms_job_id=int(std['LMSJobId']),
                description=std['Description'],
                available=bool(std['Available'])
            )

            if std['JobId']:
                dt.job_id = int(std['JobId'])

            data.append(
                dt
            )

        return data
