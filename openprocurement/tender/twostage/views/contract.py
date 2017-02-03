# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.contract import TenderUaAwardContractResource as BaseResource


@opresource(name='Tender Two Stage Contracts',
            collection_path='/tenders/{tender_id}/contracts',
            path='/tenders/{tender_id}/contracts/{contract_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender Two Stage contracts")
class TenderAwardContractResource(BaseResource):
    """ """
