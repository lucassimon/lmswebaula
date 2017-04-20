# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from lmswebaula.lms.segment.containers import *


class SegmentParse(object):

    @staticmethod
    def get_all(response):

        data = []

        ws_students = response['SegmentListDTO']['SegmentDTO']

        for std in ws_students:

            pass

        return data
