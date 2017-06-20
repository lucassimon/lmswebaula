# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetAllRQ(PaginationMixinRQ):

    pass


class GetAllStudentRS(SuccessContainerResponse):
    """

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx?s=Student&m=GetAll

    {
        Guid: 8c0a5920-c24b-4ded-b59b-d5085268cd96
        Msg: A pagina deve ser maior que 0,
        PaginationInfo: {
            NumberOfPages: None,
            Page: None,
            PageSize: None,
            TotalAmount: None
        },
        hasError: True,
        ErrorList: {
            EntityId: []
        },
        StudentListDTO: {
            StudentDTO: []
        },
            TranscriptListDTO: {
            StudentCourseSituationDTO: []
        }
    }
    """

    pass
