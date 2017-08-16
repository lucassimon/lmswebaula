# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lms.assessment.containers import *


class NoteReviewParse(object):

    @staticmethod
    def parse(response):

        data = []

        try:
            ws_data = response['NoteReviewList']['NoteReviewDTO']
        except Exception:
            return data

        for std in ws_data:

            dt = NoteReviewDTO(
                name=std['Name'],
                mastery_score=std['MasteryScore'],
                value=std['Value'],
                score=std['Score'],
                lms_evaluation_id=int(std['LMSEvaluationId']),
                lms_student_id=int(std['LMSStudentId'])
            )

            if std['EvaluationId']:
                dt.evaluation_id = std['EvaluationId']

            if std['StudentId']:
                dt.student_id = std['StudentId']

            if std['NumberOfIssues']:
                dt.number_of_issues = std['NumberOfIssues']

            if std['CorelessonStatus']:
                dt.corelesson_status = std['CorelessonStatus']

            if std['coreScoreRaw']:
                dt.core_score_raw = std['coreScoreRaw']

            if std['DateLastAccess']:
                dt.date_last_access = std['DateLastAccess']

            data.append(
                dt
            )

        return data
