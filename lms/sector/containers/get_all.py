# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lms.core.containers.pagination import PaginationMixinRQ
from lms.core.containers.response import (
    SuccessContainerResponse
)


class GetAllRQ(PaginationMixinRQ):

    pass


class GetAllSectorRS(SuccessContainerResponse):
    """
    Resposta da requisição do get_all
    """

    pass
