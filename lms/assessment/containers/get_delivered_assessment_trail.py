# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import six

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    ContainerResponse, SuccessContainerResponse
)


class GetDeliveredAssessmentTrailRQ(PaginationMixinRQ):

    _trail_class_id = None
    _lms_student_id = None
    _category = None

    def __init__(
        self,
        lms_trail_class_id,
        lms_student_id,
        page=1,
        page_size=10
    ):

        self._page = page

        self._page_size = page_size

        if lms_student_id:

            if not isinstance(lms_student_id, six.integer_types):
                raise ValueError(
                    'O lms id do estudante precisa ser um inteiro'
                )

            self._lms_student_id = lms_student_id

        if lms_trail_class_id:

            if not isinstance(lms_trail_class_id, six.integer_types):
                raise ValueError(
                    'O lms id da classe da trilha precisa ser um inteiro'
                )

            self._lms_trail_class_id = lms_trail_class_id

    @property
    def lms_student_id(self):
        return self._lms_student_id

    @lms_student_id.setter
    def lms_student_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id do estudante precisa ser um inteiro'
            )

        self._lms_student_id = value

    @property
    def lms_trail_class_id(self):
        return self._lms_trail_class_id

    @lms_trail_class_id.setter
    def lms_trail_class_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O lms id da classe da trilha precisa ser um inteiro'
            )

        self._lms_trail_class_id = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):

        self._category = value


class GetDeliveredAssessmentTrailRS(SuccessContainerResponse):
    """
    Resposta da requisição do get_delivered_assessment_trail
    """

    pass
