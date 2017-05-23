# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six


class ContainerResponse(object):

    _has_error = False
    _guid = ''
    _msg = ''

    def __init__(self, error=False, guid='', msg=''):

        self._has_error = error
        self._guid = guid
        self._msg = msg

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):

        self._has_error = value

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):

        self._guid = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):

        self._msg = value


class ErrorListResponse(object):

    _lmsid = ''
    _id = ''

    def __init__(self, lmsid, id):

        self._lmsid = lmsid
        self._id = id


class SuccessContainerResponse(ContainerResponse):

    """
    Container de sucesso
    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'Os itens precisam estar em uma lista'
            )

        self._data_list = data
        self._has_error = error
        self._guid = guid
        self._msg = msg

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):

        if not isinstance(value, list):
            raise ValueError(
                'Os itens precisam estar em uma lista'
            )

        self._data_list = value
