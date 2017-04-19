# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lmswebaula.lms.course.containers import *


class CourseParse(object):

    @staticmethod
    def get_all(response):

        data = []

        ws_students = response['CourseListDTO']['CourseDTO']

        for std in ws_students:

            data.append(
                CourseDTO(
                    folder_name=std['FolderName'],
                    frequency=float(std['Frequency']),
                    hours=float(std['Hours']),
                    media=float(std['Media']),
                    name=std['Name'],
                    name_course_menu=std['NameCourseMenu']
                )
            )

        return data
