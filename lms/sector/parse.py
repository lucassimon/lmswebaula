# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.sector.containers import *


class SectorParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['SectorListDTO']['SectorDTO']
        except Exception:
            return data

        for std in ws_data:

            dt = JobDTO(
                lms_sector_id='{0}'.format(std['LMSSectorId']),
                name=std['Name'],
            )

            if std['SectorId']:
                dt.sector_id = '{0}'.format(std['SectorId'])

            data.append(
                dt
            )

        return data
