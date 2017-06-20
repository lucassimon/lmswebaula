# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six
import pytest

from lms.course.containers import *


class CourseParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_students = response['CourseListDTO']['CourseDTO']

        except Exception:
            return data

        for std in ws_students:

            data.append(
                CourseDTO(
                    lms_course_id=int(std['LMSCourseId']),
                    folder_name=std['FolderName'],
                    frequency=float(std['Frequency']),
                    hours=float(std['Hours']),
                    media=float(std['Media']),
                    name=std['Name'],
                    name_course_menu=std['NameCourseMenu']
                )
            )

        return data
