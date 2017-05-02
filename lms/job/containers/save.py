# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class SaveRQ(object):

    _lms_job_id = ''
    _job_id = ''
    _description = ''
    _available = False

    def __init__(
        self,
        description,
        job_id,
        available=False
    ):

        if not isinstance(description, six.string_types):
            raise ValueError(
                'A descrição precisa ser uma string'
            )

        if not isinstance(job_id, six.integer_types):
            raise ValueError(
                'O cargo_id precisa ser um inteiro'
            )

        if not isinstance(available, bool):
            raise ValueError(
                'A descrição precisa ser um booleano'
            )

        self._description = description
        self._job_id = job_id
        self._available = available

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'A descrição precisa ser uma string'
            )

        self._description = value

    @property
    def lms_job_id(self):
        return self._lms_job_id

    @lms_job_id.setter
    def lms_job_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O job precisa ser um inteiro'
            )

        self._lms_job_id = value

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O cargo precisa ser um inteiro'
            )

        self._job_id = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):

        if not isinstance(value, bool):
            raise ValueError(
                'O cargo precisa ser um booleano'
            )

        self._available = value


class SaveRS(ContainerResponse):
    """
    Resposta do metodo save
    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'Os cargos precisam estar em uma lista'
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
                'Os cargos precisam estar em uma lista'
            )

        self._data_list = value
