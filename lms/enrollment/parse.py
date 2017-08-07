# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lms.enrollment.containers import *


class EnrollmentTrailClassDefaultParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws = response[
                'StudentEnrolledInTrailListDTO'
            ][
                'StudentEnrolledInTrailDTO'
            ]

        except Exception:
            return data

        for std in ws:

            data.append(
                StudentEnrolledInTrailDTO(
                    state=std['EnrollmentState'],
                    ffrom=std['From'],
                    to=std['To']
                )
            )

        return data


class GetTrailsHistoryByClassPeriodParse(object):

    @staticmethod
    def parse(response):

        data = []

        try:
            ws = response[
                'StudentTrailSituationList'
            ][
                'StudentTrailSituationDTO'
            ]

        except Exception:
            return data

        for std in ws:

            data.append(
                StudentTrailSituationDTO(
                    state=std['EnrollmentState'],
                    ffrom=std['From'],
                    to=std['To']
                )
            )

        return data