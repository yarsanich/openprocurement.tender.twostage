# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource, json_view
from openprocurement.tender.openua.views.complaint_document import TenderUaComplaintDocumentResource
from openprocurement.api.validation import (
    validate_file_update,
    validate_file_upload,
    validate_patch_document_data,
)

@opresource(name='Tender Two Stage Complaint Documents',
            collection_path='/tenders/{tender_id}/complaints/{complaint_id}/documents',
            path='/tenders/{tender_id}/complaints/{complaint_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender complaint documents")
class TenderTSComplaintDocumentResource(TenderUaComplaintDocumentResource):

    @json_view(validators=(validate_file_upload,), permission='edit_complaint')
    def collection_post(self):
        """Tender Complaint Document Upload"""
        self.request.errors.add('body', 'data', 'Tender Complaint Document upload not implemented')
        self.request.errors.status = 403
        return

    @json_view(validators=(validate_file_update,), permission='edit_complaint')
    def put(self):
        """Tender Complaint Document Update"""
        self.request.errors.add('body', 'data', 'Tender Complaint Document upload not implemented')
        self.request.errors.status = 403
        return

    @json_view(content_type="application/json", validators=(validate_patch_document_data,), permission='edit_complaint')
    def patch(self):
        """Tender Complaint Document Update"""
        self.request.errors.add('body', 'data', 'Tender Complaint Document upload not implemented')
        self.request.errors.status = 403
        return


