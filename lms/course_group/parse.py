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
                    lms_course_group_id='{0}'.format(item['LMSCourseGroupId']),
                    course_group_id=item['CourseGroupId'],
                    name=item['Name'],
                    highlighted=int(item['Highlighted']),
                )
            )

        return data
