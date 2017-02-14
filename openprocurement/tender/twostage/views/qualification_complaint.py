# -*- coding: utf-8 -*-
from openprocurement.api.models import get_now
from openprocurement.tender.twostage.utils import qualifications_resource
from openprocurement.tender.twostage.views.award_complaint import TenderTSAwardComplaintResource
from openprocurement.api.utils import (
    apply_patch,
    context_unpack,
    json_view,
    save_tender,
    set_ownership,
)
from openprocurement.api.validation import (
    validate_complaint_data,
    validate_patch_complaint_data,
)


@qualifications_resource(
    name='Tender Two Stage Qualification Complaints',
    collection_path='/tenders/{tender_id}/qualifications/{qualification_id}/complaints',
    path='/tenders/{tender_id}/qualifications/{qualification_id}/complaints/{complaint_id}',
    procurementMethodType='aboveThresholdTS',
    description="Tender Two Stage qualification complaints")
class TenderTSQualificationComplaintResource(TenderTSAwardComplaintResource):

    def complaints_len(self, tender):
        return sum([len(i.complaints) for i in tender.awards], sum([len(i.complaints) for i in tender.qualifications], len(tender.complaints)))

    @json_view(content_type="application/json", permission='create_qualification_complaint', validators=(validate_complaint_data,))
    def collection_post(self):
        """Post a complaint
        """
        self.request.errors.add('body', 'data', 'Qualifications complaints post not implemented')
        self.request.errors.status = 403
        return
    @json_view(content_type="application/json", permission='edit_complaint', validators=(validate_patch_complaint_data,))
    def patch(self):
        """Patch the complaint
        """
        self.request.errors.add('body', 'data', 'Qualifications complaints patch not implemented')
        self.request.errors.status = 403
