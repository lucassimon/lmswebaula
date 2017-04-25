# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByDescriptionRQ(object):

    _description = None

    def __init__(self, description):

        if not isinstance(description, six.string_types):
            raise ValueError(
                'A descrição precisa ser uma string'
            )

        self._description = description

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'O descrição precisa ser uma string'
            )

        self._description = value
