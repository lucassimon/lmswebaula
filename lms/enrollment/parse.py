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

            student = StudentTrailSituationDTO(
                lms_student_id=std['LMSStudentId'],
                lms_trail_id=std['LMSTrailId'],
                lms_trail_class_id=std['LMSTrailclassId'],
                percent_utilization=std['PercentUtilization'],
                percent_conclusion=std['PercentConclusion'],
                finalized=std['Finalized']
            )

            if std['StudentId']:
                student.student_id = std['StudentId']

            if std['TrailId']:
                student.trail_id = std['TrailId']

            if std['TrailClassId']:
                student.trail_class_id = std['TrailClassId']

            if std['ConcludedOn']:
                student.concluded_on = std['ConcludedOn']

            if std['AccessedOn']:
                student.accessed_on = std['AccessedOn']

            if std['FirstAccess']:
                student.first_access = std['FirstAccess']

            if std['RegistrationDate']:
                student.registration_date = std['RegistrationDate']

            if std['TrailClassDateBegin']:
                student.trail_class_date_begin = std['TrailClassDateBegin']

            if std['TrailClassDateEnd']:
                student.trail_class_date_end = std['TrailClassDateEnd']

            data.append(
                student
            )

        return data
