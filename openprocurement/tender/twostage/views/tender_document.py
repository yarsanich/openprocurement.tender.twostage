# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.tender_document import TenderUaDocumentResource


@opresource(name='Tender Two Stage Documents',
            collection_path='/tenders/{tender_id}/documents',
            path='/tenders/{tender_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender Two Stage related binary files (PDFs, etc.)")
class TenderTSDocumentResource(TenderUaDocumentResource):
    pass
