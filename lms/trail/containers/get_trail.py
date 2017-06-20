# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetTrailRQ(object):

    _trail_id = None
    _lms_trail_id = None

    def __init__(self, lms_trail_id=None, trail_id=None):

        if lms_trail_id:

            if not isinstance(lms_trail_id, six.integer_types):
                raise ValueError(
                    'O lms id da trilha precisa ser um inteiro'
                )

            self._lms_trail_id = lms_trail_id

        if trail_id:

            if not isinstance(trail_id, six.integer_types):
                raise ValueError(
                    'O id da trilha precisa ser um inteiro'
                )

            self._trail_id = trail_id

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


class GetTrailRS(SuccessContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Trail&m=GetTrail

    """

    pass
