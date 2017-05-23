# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.trail.containers.response import (
    TrailDTO
)


class TrailParse(object):

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['TrailListDTO']['TrailDTO']
        except Exception:
            return data

        for std in ws_data:

            item = TrailDTO(
                lms_trail_id='{0}'.format(std['LMSTrailId']),
                name=std['Name'],
                description=std['Description'],
                lms_activity_group_id=std['LMSActivityGroupId'],
                lms_group_id=std['LMSGroupId'],
                group_id=std['GroupId'],
                active=std['Active'],
                hours=std['Hours']
            )

            if std['TrailId']:
                item.trail_id = '{0}'.format(std['TrailId'])

            data.append(
                item
            )

        return data
