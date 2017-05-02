# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.level.containers import *


class LevelParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['LevelListDTO']['LevelDTO']
        except Exception:
            return data

        for std in ws_data:

            dt = LevelDTO(
                lms_level_id='{0}'.format(std['LMSLevelId']),
                name=std['Name'],
                order=std['Order']
            )

            if std['LevelId']:
                dt.level_id = '{0}'.format(std['LevelId'])

            data.append(
                dt
            )

        return data
