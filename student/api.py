# -*- coding: utf-8 -*-

from rpc import (
    RPC as StudentRpc
)

from containers.students import (
    StudentRS
)


class API(object):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    def __init__(self, passport):

        if not passport:
            raise ValueError(
                'E necessário passar um passport'
            )

        self.rpc = StudentRpc(passport=passport)

    def get_all(self):
        """
        Retorna todos os estudantes
        """

        try:
            response = self.rpc.get_all()
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        students = StudentRS()

        # tratar os dados

        # Retornar o student response

        return students
