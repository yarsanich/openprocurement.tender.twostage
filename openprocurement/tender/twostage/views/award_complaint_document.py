# -*- coding: utf-8 -*-
from openprocurement.tender.openua.views.award_complaint_document import TenderUaAwardComplaintDocumentResource
from openprocurement.api.utils import (
    json_view,
    opresource
)
from openprocurement.api.validation import (
    validate_file_update,
    validate_file_upload,
    validate_patch_document_data
)

@opresource(name='Tender Two Stage Award Complaint Documents',
            collection_path='/tenders/{tender_id}/awards/{award_id}/complaints/{complaint_id}/documents',
            path='/tenders/{tender_id}/awards/{award_id}/complaints/{complaint_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender award complaint documents")
class TenderTSAwardComplaintDocumentResource(TenderUaAwardComplaintDocumentResource):
    @json_view(permission='edit_complaint', validators=(validate_file_upload,))
    def collection_post(self):
        """Tender Award  Complaint Document Upload"""
        self.request.errors.add('body', 'data', 'Upload award complaint documents not implemented')
        self.request.errors.status = 403
        return
    @json_view(permission='edit_complaint', validators=(validate_file_update,))
    def put(self):
        """Tender Award Complaint Document Update"""
        self.request.errors.add('body', 'data', 'Update award complaint documents not implemented')
        self.request.errors.status = 403
        return

    @json_view(permission='edit_complaint', content_type="application/json", validators=(validate_patch_document_data,))
    def patch(self):
        """Tender Award Complaint Document Update"""
        self.request.errors.add('body', 'data', 'Update award complaint documents not implemented')
        self.request.errors.status = 400
        return

