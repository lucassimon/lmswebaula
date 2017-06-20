# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
                lms_trail_id=int(std['LMSTrailId']),
                name=std['Name'],
                description=std['Description'],
                lms_activity_group_id=int(std['LMSActivityGroupId']),
                lms_group_id=int(std['LMSGroupId']),
                group_id=int(std['GroupId']),
                active=std['Active'],
                hours=std['Hours']
            )

            if std['TrailId']:
                item.trail_id = int(std['TrailId'])

            data.append(
                item
            )

        return data
