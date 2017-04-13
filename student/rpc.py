# -*- coding: utf-8 -*-
#
from zeep import Client


class RPC(object):

    formato_data = '%Y-%m-%d'
    formato_hora = '%H:%M:%S'
    cache = None

    _passport = ''

    def __init__(self, passport):

        self._passport = passport

    def get_all(self):

        request = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')

        try:
            response = request.service.GetAll(
                passport=self._passport
            )
        except Exception as e:
            raise e

        return response