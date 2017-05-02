# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six


from lms.core.containers.response import (
    ContainerResponse, ErrorListResponse
)


class SaveRQ(object):

    _lms_competence_id = ''
    _competence_id = ''
    _name = ''

    def __init__(
        self,
        name,
        competence_id,
    ):

        if not isinstance(name, six.string_types):
            raise ValueError(
                'O nome do nivel precisa ser uma string'
            )

        if not isinstance(competence_id, six.integer_types):
            raise ValueError(
                'O nivel_id precisa ser um inteiro'
            )

        self._name = name
        self._competence_id = competence_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, six.string_types):
            raise ValueError(
                'O nome do nivel precisa ser uma string'
            )

        self._name = value

    @property
    def lms_competence_id(self):
        return self._lms_competence_id

    @lms_competence_id.setter
    def lms_competence_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O nivel precisa ser um inteiro'
            )

        self._lms_competence_id = value

    @property
    def competence_id(self):
        return self._competence_id

    @competence_id.setter
    def competence_id(self, value):

        if not isinstance(value, six.integer_types):
            raise ValueError(
                'O nivel precisa ser um inteiro'
            )

        self._competence_id = value


class SaveRS(ContainerResponse):
    """
    Resposta do metodo save
    """

    _data_list = []

    def __init__(self, error=True, guid='', msg='', data=[]):

        if not isinstance(data, list):
            raise ValueError(
                'A competencia precisa estar em uma lista'
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
                'Os nivels precisam estar em uma lista'
            )

        self._data_list = value
