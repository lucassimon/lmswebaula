# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lmswebaula.lms.student.containers.response import (
    StudentDTO
)


class StudentParse(object):

    @staticmethod
    def get_all(response):

        students = []
        ws_students = response['StudentListDTO']['StudentDTO']

        for std in ws_students:

            students.append(
                StudentDTO(
                    cpf=std['CPF'],
                    date_of_birth=std['DateOfBirth'],
                    email=std['Email'],
                    login=std['Login'],
                    name=std['Name'],
                    sex=std['Sex'],
                    status=std['Status'],
                )
            )

        return students
