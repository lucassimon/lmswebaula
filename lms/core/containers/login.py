# -*- coding: utf-8 -*-
import six


class LoginRQ(object):

    _passaport = None
    _url = None

    def __init__(self, passport, url):

        if not passport:
            raise ValueError(
                'E necessário passar um passport'
            )

        if not isinstance(passport, six.string_types):
            raise ValueError(
                'O passport precisa ser uma string'
            )

        if not url:
            raise ValueError(
                'E necessário passar uma url do serviço'
            )

        if not isinstance(url, six.string_types):
            raise ValueError(
                'A url do servico precisa ser uma string'
            )

        self._passaport = passport
        self._url = url

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'O passport precisa ser uma string'
            )
        else:
            self._passport = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'A url do servico precisa ser uma string'
            )
        else:
            self._url = value
