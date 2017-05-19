# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByIdRQ(object):

    _competence_id = None
    _lms_competence_id = None

    def __init__(self, lms_competence_id, competence_id=None):

        self._lms_competence_id = lms_competence_id
        self._competence_id = competence_id

    @property
    def lms_competence_id(self):
        return self._lms_competence_id

    @lms_competence_id.setter
    def lms_competence_id(self, value):

        self._lms_competence_id = value

    @property
    def competence_id(self):
        return self._competence_id

    @competence_id.setter
    def competence_id(self, value):

        self._competence_id = value