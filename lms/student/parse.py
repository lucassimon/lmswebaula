# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lmswebaula.lms.student.containers.response import (
    StudentDTO
)


class StudentParse(object):

    @staticmethod
    def get_all(response):

        data = []
        ws_students = response['StudentListDTO']['StudentDTO']

        for std in ws_students:

            student = StudentDTO(
                lms_student_id=std['LMSStudentId'],
                cpf=std['CPF'],
                date_of_birth=std['DateOfBirth'],
                email=std['Email'],
                login=std['Login'],
                name=std['Name'],
                sex=std['Sex'],
                status=std['Status'],
            )

            if std['StudentId']:
                student.student_id = std['StudentId']

            data.append(
                student
            )

        return data
