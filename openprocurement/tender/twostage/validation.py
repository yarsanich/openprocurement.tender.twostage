# -*- coding: utf-8 -*-
from openprocurement.api.validation import validate_data
from openprocurement.tender.twostage.models import Qualification


def validate_patch_qualification_data(request):
    return validate_data(request, Qualification, True)
