# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


class GetByLoginRQ(object):
    """
    O login do estudante é seu CPF
    """

    _login = None

    def __init__(self, login):

        self._login = login

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):

        self._login = value
