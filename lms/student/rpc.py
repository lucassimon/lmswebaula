# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import datetime

from zeep import Client
from lmswebaula.lms.student.containers import *

import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})


class RPC(object):

    formato_data = '%Y-%m-%d'
    formato_hora = '%H:%M:%S'

    def __init__(self, login, passport):

        self._login = login
        self._passport = passport

    def get_all(self, paginate):

        if not isinstance(paginate, GetAllRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        request = Client(self._login.url)

        try:
            response = request.service.GetAll(
                passport=self._passport,
                page=paginate.page,
                pageSize=paginate.page_size
            )
        except Exception as e:
            raise e

        return response

    def save(self, data):

        if not isinstance(data, StudentDTO):
            raise ValueError(
                "Não existe dados para o estudante"
            )

        request = Client(self._login.url)

        save_type = request.get_element('ns0:Save')

        array_student_dto = request.get_type('ns5:ArrayOfStudentDTO')

        student_dto = request.get_type('ns5:StudentDTO')

        student = student_dto(
            AdmissionDate=data.convert_to_post().get('AdmissionDate'),
            BranchId=data.convert_to_post().get('BranchId'),
            CEP=data.convert_to_post().get('CEP'),
            CPF=data.convert_to_post().get('CPF'),
            Celular=data.convert_to_post().get('Celular'),
            City=data.convert_to_post().get('City'),
            Company=data.convert_to_post().get('Company'),
            Complement=data.convert_to_post().get('Complement'),
            DDD=data.convert_to_post().get('DDD'),
            DateOfBirth=datetime.datetime(1985, 12, 4, 0, 0),
            DepartmentId=data.convert_to_post().get('DepartmentId'),
            District=data.convert_to_post().get('District'),
            Email=data.convert_to_post().get('Email'),
            ForeingStudent=False,
            JobId=data.convert_to_post().get('JobId'),
            LMSBranchId=data.convert_to_post().get('DepartmentId'),
            LMSDepartmentId=data.convert_to_post().get('DepartmentId'),
            LMSFreeTable1=data.convert_to_post().get('DepartmentId'),
            LMSFreeTable2=data.convert_to_post().get('DepartmentId'),
            LMSFreeTable5=data.convert_to_post().get('DepartmentId'),
            LMSJobId=data.convert_to_post().get('DepartmentId'),
            LMSMaritalStatusId=data.convert_to_post().get('DepartmentId'),
            LMSSchoolingId=data.convert_to_post().get('DepartmentId'),
            LMSStudentId=data.convert_to_post().get('DepartmentId'),
            LMSTeamId=data.convert_to_post().get('DepartmentId'),
            LevelList=data.convert_to_post().get('DepartmentId'),
            Login=data.convert_to_post().get('email'),
            MaritalStatusId=data.convert_to_post().get('DepartmentId'),
            Name='Teste WebAula Corporativo',
            NickName=data.convert_to_post().get('DepartmentId'),
            Number=data.convert_to_post().get('DepartmentId'),
            Password=data.convert_to_post().get('DepartmentId'),
            Registration=data.convert_to_post().get('DepartmentId'),
            SchoolingId=data.convert_to_post().get('DepartmentId'),
            SectorList=data.convert_to_post().get('DepartmentId'),
            Sex='Male',
            StateAbbreviation=data.convert_to_post().get('DepartmentId'),
            StudentId=data.convert_to_post().get('DepartmentId'),
            TeamId=data.convert_to_post().get('DepartmentId'),
        )

        # array_student_dto(StudentDTO=student)

        # save = save_type(
        #     passport=self._passport,
        #     studentListDTO=
        # )

        try:
            response = request.service.Save(
                passport=self._passport,
                studentListDTO=array_student_dto(student)
            )

        except Exception as e:
            raise e

        return response
