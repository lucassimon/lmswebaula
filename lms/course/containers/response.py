# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class CourseDTO(object):

    _lms_course_id = 0
    _course_id = None
    _lms_group_id = 0
    _name = ""
    _folder_name = ""
    _term = ""
    _evaluation_has = False
    _name_course_menu = ""
    _pre_requirements = 0
    _media = 0
    _frequency = 0
    _has_certified = False
    _course_class_type = None
    _has_pre_test = False
    _class_room_course = False
    _completion_certificate = False
    _pre_registration = False
    _date_begin_pre_registration = None
    _date_end_pre_registration = None
    _hours = 0
    _provider = ""
    _description = ""
    _re_enrollment = 0
    _access_to_term_pos = False
    _scorm_compliant = False
    _have_recycling = False
    _has_media = False
    _has_flash = False
    _displays_the_catalog = False
    _segment_pre_registration = None
    _time_travel_news = ""
    _group_id = ""
    _lms_group_id = None
    _amount_questions = 0
    _follow_schedule = 0
    _full_screen = False
    _pre_registration_validity = None
    _order = 0
    _demonstration_active = False
    _width_room = 0
    _height_room = 0
    _allows_re_enrollment = False
    _aicccompilant = False
    _status = False

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

    @property
    def name_course_menu(self):
        return self._name_course_menu

    @name_course_menu.setter
    def name_course_menu(self, value):

        self._name_course_menu = value

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):

        self._group_id = value

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):

        self._course_id = value

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):

        self._hours = value

    @property
    def media(self):
        return self._media

    @media.setter
    def media(self, value):

        self._media = value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):

        self._frequency = value

    @property
    def sector_list(self):
        return self._sector_list

    @sector_list.setter
    def sector_list(self, value):

        self._sector_list = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        self._status = value
