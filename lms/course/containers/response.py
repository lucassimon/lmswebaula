# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class CourseDTO(object):

    _aicccompilant = False
    _access_to_term_pos = False,
    _allows_re_enrollment = False,
    _amount_questions = "",
    _class_room_course = True,
    _competence_list = None,
    _completion_certificate = False,
    _course_class_type = "FreeClassesAndCourseClasses",
    _course_id = None,
    _course_level_job_list = None,
    _date_begin_pre_registration = None,
    _date_end_pre_registration = None,
    _demonstration_active = False,
    _description = None,
    _displays_the_catalog = False,
    _evaluation_has = False,
    _folder_name = "",
    _follow_schedule = "",
    _frequency = 75
    _full_screen = False,
    _group_id = None,
    _has_flash = True,
    _has_media = False,
    _has_pre_test = False,
    _has_certified = False,
    _have_recycling = False,
    _height_room = "",
    _hours = ""
    _lms_course_id = "",
    _lms_group_id = "",
    _media = "",
    _name = "",
    _name_course_menu = ""
    _order = "",
    _pre_registration = False,
    _pre_registration_validity = "",
    _pre_requirements = "",
    _pre_requisite_courses = None,
    _provider = None,
    _re_enrollment = "",
    _scorm_compliant = True,
    _sector_list = None,
    _segment_pre_registration = "",
    _status = True,
    _term = "",
    _time_travel_news = None,
    _width_room = ""

    def __init__(
        self,
        lms_course_id,
        folder_name,
        frequency,
        hours,
        media,
        name,
        name_course_menu
    ):
        self._lms_course_id = lms_course_id
        self._folder_name = folder_name
        self._frequency = frequency
        self._hours = hours
        self._media = media
        self._name = name
        self._name_course_menu = name_course_menu

    @property
    def folder_name(self):
        return self._folder_name

    @folder_name.setter
    def folder_name(self, value):

        self._folder_name = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def lms_course_id(self):
        return self._lms_course_id

    @lms_course_id.setter
    def lms_course_id(self, value):

        self._lms_course_id = value

    def convert_to_post(self):
        pass
