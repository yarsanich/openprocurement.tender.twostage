# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.award import TenderUaAwardResource as BaseResource


@opresource(name='Tender Two Stage Awards',
            collection_path='/tenders/{tender_id}/awards',
            path='/tenders/{tender_id}/awards/{award_id}',
            description="Tender Two Stage awards",
            procurementMethodType='aboveThresholdTS')
class TenderAwardResource(BaseResource):
    """ Two stage award resource """
