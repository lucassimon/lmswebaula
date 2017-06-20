# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six

from lms.core.containers.response import (
    SuccessContainerResponse, ErrorListResponse
)

from lms.course_group.containers.response import CourseGroupDTO


class SaveRQ(CourseGroupDTO):

    def __init__(
        self,
        highlighted,
        name,
        course_group_id
    ):

        if not isinstance(course_group_id, six.integer_types):
            raise ValueError(
                'O id da grupo de curso precisa ser um inteiro'
            )

        self._course_group_id = course_group_id

        self._highlighted = highlighted

        self._name = name


class SaveRS(SuccessContainerResponse):

    pass
