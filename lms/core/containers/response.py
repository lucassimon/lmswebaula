# -*- coding: utf-8 -*-


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
