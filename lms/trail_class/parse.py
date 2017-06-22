# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from lms.trail_class.containers.response import (
    TrailClassDTO,
    StudentTrailClass
)


class TrailClassParse(object):

    @staticmethod
    def get_all(response):

        students = []

        data = []

        try:
            ws_data = response['TrailClassList']['TrailClassDTO']['Students']
        except Exception:
            return data

        for std in ws_data:

            item = StudentTrailClass(
                lms_student_id=int(std['LMSStudentId']),
                name=std['Name'],
                state=std['State'],
            )

            if std['StudentId']:
                item.student_id = std['StudentId']

        try:
            ws_data = response['TrailClassList']['TrailClassDTO']
        except Exception:
            return data

        for std in ws_data:

            item = TrailClassDTO(
                lms_trail_class_id=int(std['LMSTrailClassId']),
                lms_trail_id=int(std['LMSTrailId']),
                name=std['Name'],
                description=std['Description'],
                time_from=std['TimeFrom'],
                time_to=std['TimeTo'],
                students=students,
            )

            if std['TrailId']:
                item.trail_id = std['TrailId']

            if std['TrailClassId']:
                item.trail_class_id = std['TrailClassId']

            data.append(
                item
            )

        return data
