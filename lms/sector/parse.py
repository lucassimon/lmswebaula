# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

            dt = SectorDTO(
                lms_sector_id=int(std['LMSSectorId']),
                name=std['Name'],
            )

            if std['SectorId']:
                dt.sector_id = int(std['SectorId'])

            data.append(
                dt
            )

        return data
