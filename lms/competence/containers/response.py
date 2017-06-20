# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

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

        if not isinstance(lms_competence_id, six.integer_types):
            raise ValueError(
                'O lms id da competencia precisa ser um inteiro'
            )

        self._lms_competence_id = lms_competence_id
        self._name = name

        if competence_id:

            if not isinstance(competence_id, six.integer_types):
                raise ValueError(
                    'O id da competencia precisa ser um inteiro'
                )

            self._competence_id = competence_id

    @property
    def lms_competence_id(self):
        return self._lms_competence_id

    @lms_competence_id.setter
    def lms_competence_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da competencia precisa ser um inteiro'
            )

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

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da competencia precisa ser um inteiro'
            )

        self._competence_id = value
