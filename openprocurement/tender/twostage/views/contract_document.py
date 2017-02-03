# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.contract_document import TenderUaAwardContractDocumentResource as BaseResource


@opresource(name='Tender Two Stage Contract Documents',
            collection_path='/tenders/{tender_id}/contracts/{contract_id}/documents',
            path='/tenders/{tender_id}/contracts/{contract_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender contract documents")
class TenderAwardContractDocumentResource(BaseResource):
    """ Tender Award Contract Document """
