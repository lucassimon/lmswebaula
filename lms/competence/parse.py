# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.competence.containers import *


class CompetenceParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['CompetenceListDTO']['CompetenceDTO']
        except Exception:
            return data

        for std in ws_data:

            dt = CompetenceDTO(
                lms_competence_id=int(std['LMSCompetenceId']),
                name=std['Name']
            )

            if std['CompetenceId']:
                dt.competence_id = int(std['CompetenceId'])

            data.append(
                dt
            )

        return data
