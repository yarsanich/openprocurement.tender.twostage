# -*- coding: utf-8 -*-
from openprocurement.api.utils import (opresource,
                                       json_view,
                                       context_unpack)
from openprocurement.tender.openua.views.complaint import TenderUaComplaintResource
from openprocurement.api.validation import (
    validate_complaint_data,
    validate_patch_complaint_data,
)
@opresource(name='Tender Two Stage Complaints',
            collection_path='/tenders/{tender_id}/complaints',
            path='/tenders/{tender_id}/complaints/{complaint_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender Two Stage complaints")
class TenderTSComplaintResource(TenderUaComplaintResource):

    def complaints_len(self, tender):
        return sum([len(i.complaints) for i in tender.awards], sum([len(i.complaints) for i in tender.qualifications], len(tender.complaints)))

    @json_view(content_type="application/json", validators=(validate_complaint_data), permission='create_complaint')
    def collection_post(self):
        """Post a complaint"""
        self.request.errors.add('body', 'data', 'Complaint addition not implemented')
        self.request.errors.status = 403

    @json_view(content_type="application/json", validators=(validate_patch_complaint_data,), permission='edit_complaint')
    def patch(self):
        """Post a complaint resolution"""
        self.request.errors.add('body', 'data', 'Complaint addition not implemented')
        self.request.errors.status = 403

