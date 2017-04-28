# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.klass.containers import *


class KlassParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_students = response['ClassListDTO']['ClassDTO']

        except Exception:
            return data

        for std in ws_students:

            data.append(
                DataDTO(
                    name=std['Name'],
                    lms_class_id=int(std['LMSClassId']),
                    lms_course_id=int(std['LMSCourseId']),
                    maximum_students=std['MaximumStudents'],
                    start_time=std['StartTime'],
                    end_time=std['EndTime']
                )
            )

        return data
