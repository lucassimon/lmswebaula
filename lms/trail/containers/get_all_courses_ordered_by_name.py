# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetAllCoursesOrderedByNameRQ(PaginationMixinRQ):

    pass


class GetAllCoursesOrderedByNameRS(SuccessContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Trail&m=GetTrail

    """

    pass
