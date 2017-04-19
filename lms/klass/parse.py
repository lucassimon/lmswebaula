# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lmswebaula.lms.klass.containers import *


class KlassParse(object):

    @staticmethod
    def get_all(response):

        data = []

        ws_students = response['ClassListDTO']['ClassDTO']

        for std in ws_students:

            data.append(
                DataDTO(
                    name=std['Name'],
                    lms_class_id=std['LMSClassId'],
                    lms_course_id=std['LMSCourseId'],
                    maximum_students=std['MaximumStudents'],
                    start_time=std['StartTime'],
                    end_time=std['EndTime']
                )
            )

        return data
