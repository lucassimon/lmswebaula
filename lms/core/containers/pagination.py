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

        if value <= 0:
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

        if value <= 0:
            raise ValueError(
                'O tamanho da pagina precisa ser maior que zero'
            )
        else:
            self._page_size = value


class PaginationMixinRS(object):
    """
    PaginationInfo': {
        'NumberOfPages': 1L,
        'Page': 1L,
        'PageSize': 12L,
        'TotalAmount': 3L
    }
    """
    _number_of_pages = 1
    _page = 1
    _page_size = 30
    _total_amount = 1

    def __init__(self, number_of_pages, page, page_size, total_amount):

        self._page = page
        self._page_size = page_size
        self._number_of_pages = number_of_pages
        self._total_amount = total_amount

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

        if value <= 0:
            raise ValueError(
                'O tamanho da pagina precisa ser maior que zero'
            )
        else:
            self._page_size = value

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O número de paginas precisa ser um inteiro'
            )

        if value <= 0:
            raise ValueError(
                'O número de paginas precisa ser maior que zero'
            )
        else:
            self._number_of_pages = value

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O total de itens precisa ser um inteiro'
            )

        if value <= 0:
            raise ValueError(
                'O total de itens precisa ser maior que zero'
            )
        else:
            self._total_amount = value


class PaginationParse(object):

    @staticmethod
    def parse(response):

        data = PaginationMixinRS(
            number_of_pages=response['NumberOfPages'],
            page=response['Page'],
            page_size=response['PageSize'],
            total_amount=response['TotalAmount']
        )

        return data
