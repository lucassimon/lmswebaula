# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six


class PaginationMixinRQ(object):

    _page = 1
    _page_size = 2

    def __init__(self, page=1, page_size=12):

        self._page = page
        self._page_size = page_size

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'A pagina precisa ser um inteiro'
            )
        elif value > 0:
            raise ValueError(
                'A pagina precisa ser maior que zero'
            )
        else:
            self._page = value

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O tamanho da pagina precisa ser um inteiro'
            )
        elif value > 0:
            raise ValueError(
                'O tamanho da pagina precisa ser maior que zero'
            )
        else:
            self._page_size = value
