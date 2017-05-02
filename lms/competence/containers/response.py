# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class CompetenceDTO(object):

    _lms_competence_id = "",
    _competence_id = "",
    _name = ""
    _order = 0

    def __init__(
        self,
        lms_competence_id,
        name,
        competence_id=None,
    ):
        self._lms_competence_id = lms_competence_id
        self._name = name

        if competence_id:
            self._competence_id = competence_id

    @property
    def lms_competence_id(self):
        return self._lms_competence_id

    @lms_competence_id.setter
    def lms_competence_id(self, value):

        self._lms_competence_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value

    @property
    def competence_id(self):
        return self._competence_id

    @competence_id.setter
    def competence_id(self, value):

        self._competence_id = value
