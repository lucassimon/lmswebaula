# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse
)


class SaveRQ(object):

    _lms_trail_id = 0
    _trail_id = None
    _name = ''
    _description = ''
    _lms_activity_group_id = 0
    _lms_group_id = 0
    _group_id = 0
    _active = False
    _trail_steps = []
    _hours = 0
    _trail_level_jobs = []
    _sectors = []
    _competences = []
    _pre_requisites = []

    def __init__(
        self,
        lms_trail_id,
        trail_id,
        name,
        description,
        active
    ):

        if not isinstance(lms_trail_id, six.integer_types):
            raise ValueError(
                'O lms id da trilha precisa ser um inteiro'
            )

        self._lms_trail_id = lms_trail_id

        if trail_id:

            if not isinstance(lms_trail_id, six.integer_types):
                raise ValueError(
                    'O id da trilha precisa ser um inteiro'
                )

            self._trail_id = trail_id

        self._name = name

        self._description = description

        self._active = active

    @property
    def lms_trail_id(self):
        return self._lms_trail_id

    @lms_trail_id.setter
    def lms_trail_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da trilha precisa ser um inteiro'
            )

        self._lms_trail_id = value

    @property
    def trail_id(self):
        return self._trail_id

    @trail_id.setter
    def trail_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id da trilha precisa ser um inteiro'
            )

        self._trail_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        self._description = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):

        self._active = value


class SaveRS(SuccessContainerResponse):

    pass
