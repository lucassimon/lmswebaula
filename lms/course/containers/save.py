# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
)

from lms.course.containers.response import CourseDTO


class SaveRQ(CourseDTO):

    def __init__(
        self,
        name,
        name_course_menu,
        group_id,
        course_id,
        hours,
        media,
        frequency,
        sector_list,
        status,
        course_class_type
    ):
        self._name = name
        self._name_course_menu = name_course_menu
        self._group_id = group_id
        self._course_id = course_id
        self._hours = hours
        self._media = media
        self._frequency = frequency
        self._sector_list = sector_list
        self._status = status
        self._course_class_type = course_class_type


class SaveRS(SuccessContainerResponse):

    pass
