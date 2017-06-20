# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    ContainerResponse
)


class StatusRQ(object):

    _student_id = None
    _lms_student_id = None
    _active = True

    def __init__(self, lms_student_id, active, student_id=None):

        if not isinstance(active, bool):
            raise ValueError(
                'O valor ativo precisa ser um booleano'
            )
        else:
            self._active = active

        if not isinstance(lms_student_id, six.integer_types):
            raise ValueError(
                'O id do estudante precisa ser informado como inteiro long'
            )
        else:
            self._lms_student_id = lms_student_id

        if student_id:

            if not isinstance(student_id, six.integer_types):
                raise ValueError(
                    'O id legado do estudante precisa ser um iteiro long'
                )
            else:
                self._student_id = student_id

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'O id do estudante precisa ser um inteiro'
            )
        else:
            self._lms_student_id = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):

        if not isinstance(value, bool):
            raise ValueError(
                'O valor ativo precisa ser um booleano'
            )
        else:
            self._active = value


class StatusRS(ContainerResponse):
    """
    {
        'Guid': '6bdcaec4-bf3f-4349-8242-213b37e4f449',
        'Msg': None,
        'PaginationInfo': {
            'NumberOfPages': None,
            'Page': None,
            'PageSize': None,
            'TotalAmount': None
        },
        'hasError': False
    }

    """

    pass
