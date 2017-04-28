# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)

from lms.course.containers.response import CourseDTO


class CourseRQ(CourseDTO):

    pass


class CourseRS(ContainerResponse):

    pass
