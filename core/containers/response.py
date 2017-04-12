# -*- coding: utf-8 -*-


class ContainerResponse(object):

    _error = False
    _guid = ''
    _msg = ''

    def __init__(self, error=False, guid='', msg=''):

        self._error = error
        self._guid = guid
        self._msg = msg


class ErrorListResponse(object):

    _lmsid = ''
    _id = ''

    def __init__(self, lmsid, id):

        self._lmsid = lmsid
        self._id = id
