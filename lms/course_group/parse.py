# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.course_group.containers import *


class CourseGroupParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_items = response['CourseGroupListDTO']['CourseGroupDTO']

        except Exception:
            return data

        for item in ws_items:
            data.append(
                CourseGroupDTO(
                    lms_course_group_id=int(item['LMSCourseGroupId']),
                    course_group_id=int(item['CourseGroupId']),
                    name=item['Name'],
                    highlighted=int(item['Highlighted']),
                )
            )

        return data
