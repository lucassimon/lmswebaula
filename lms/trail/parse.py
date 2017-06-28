# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from lms.trail.containers.response import (
    TrailDTO, GroupTrailDTO
)


class TrailParse(object):

    @staticmethod
    def get_all(response, result=None):

        data = []

        if result:
            ws_data = result
        else:
            try:
                ws_data = response['TrailListDTO']['TrailDTO']
            except Exception:
                return data

        for std in ws_data:

            item = TrailDTO(
                lms_trail_id=int(std['LMSTrailId']),
                name=std['Name'],
                description=std['Description'],
                active=std['Active']
            )

            if std['TrailId']:
                item.trail_id = int(std['TrailId'])

            if std['GroupId']:

                item.group_id = std['GroupId']

            if std['LMSGroupId']:

                item.lms_group_id = std['LMSGroupId']

            if std['Hours']:

                item.hours = std['Hours']

            data.append(
                item
            )

        return data


class GroupTrailCustomizedParse(object):
    """
    {
        'Msg': u'Opera\xe7\xe3o realizada com sucesso.',
        'PaginationInfo': {
            'NumberOfPages': 385L,
            'Page': 1L,
            'PageSize': 1L,
            'TotalRecords': 385L
        },
        'Result': {
            'Course': [
                {
                    'CourseId': 138L,
                    'CourseName': u' \xc1rea de Gest\xe3o/MBA'
                }
            ]
        },
        'hasError': False
    }
    """

    @staticmethod
    def get_all(response):

        data = []

        try:
            ws_data = response['Result']['Course']
        except Exception:
            return data

        for std in ws_data:

            item = GroupTrailDTO(
                name=std['CourseName']
            )

            if std['CourseId']:
                item.group_trail_id = int(std['CourseId'])

            data.append(
                item
            )

        return data
