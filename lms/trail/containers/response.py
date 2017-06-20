# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class TrailDTO(object):

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
                'O lms id da trilha precisa ser um inteiro'
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

    @property
    def lms_activity_group_id(self):
        return self._lms_activity_group_id

    @lms_activity_group_id.setter
    def lms_activity_group_id(self, value):

        self._lms_activity_group_id = value

    @property
    def lms_group_id(self):
        return self._lms_group_id

    @lms_group_id.setter
    def lms_group_id(self, value):

        self._lms_group_id = value

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):

        self._group_id = value

    @property
    def trail_steps(self):
        return self._trail_steps

    @trail_steps.setter
    def trail_steps(self, value):

        self._trail_steps = value

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):

        self._hours = value

    @property
    def trail_level_jobs(self):
        return self._trail_level_jobs

    @trail_level_jobs.setter
    def trail_level_jobs(self, value):

        self._trail_level_jobs = value

    @property
    def sectors(self):
        return self._sectors

    @sectors.setter
    def sectors(self, value):

        self._sectors = value

    @property
    def competences(self):
        return self._competences

    @competences.setter
    def competences(self, value):

        self._competences = value

    @property
    def pre_requisites(self):
        return self._pre_requisites

    @pre_requisites.setter
    def pre_requisites(self, value):

        self._pre_requisites = value
