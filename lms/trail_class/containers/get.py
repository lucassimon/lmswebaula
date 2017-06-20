# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetRQ(object):

    _trail_class_id = None
    _lms_trail_class_id = None

    def __init__(self, trail_class_id=None, lms_trail_class_id=None,):

        if not isinstance(lms_trail_class_id, six.integer_types):
            raise ValueError(
                'O lms id da turma da trilha precisa ser um inteiro'
            )

        if not isinstance(trail_class_id, six.integer_types):
            raise ValueError(
                'O id da turma da trilha precisa ser um inteiro'
            )

        self._lms_trail_class_id = lms_trail_class_id
        self._trail_class_id = trail_class_id

    @property
    def lms_trail_class_id(self):
        return self._lms_trail_class_id

    @lms_trail_class_id.setter
    def lms_trail_class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da turma da trilha precisa ser um inteiro'
            )

        self._lms_trail_class_id = value

    @property
    def trail_class_id(self):
        return self._trail_class_id

    @trail_class_id.setter
    def trail_class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O id da turma da trilha precisa ser um inteiro'
            )

        self._trail_class_id = value


class GetRS(SuccessContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Trail&m=GetTrail

    """

    pass
