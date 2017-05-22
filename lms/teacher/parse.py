# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.teacher.containers.response import (
    TeacherDTO
)


class TeacherParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['TeacherListDTO']['TeacherDTO']
        except Exception:
            return data

        for std in ws_data:

            item = TeacherDTO(
                lms_teacher_id='{0}'.format(std['LMSTeacherId']),
                cpf=std['Cpf'],
                email=std['Email'],
                password=std['Password'],
                job=std['Job'],
                coordinator=std['Coordinator'],
                name=std['Name'],
                status=std['Status']
            )

            if std['TeacherId']:
                item.teacher_id = '{0}'.format(std['TeacherId'])

            data.append(
                item
            )

        return data
