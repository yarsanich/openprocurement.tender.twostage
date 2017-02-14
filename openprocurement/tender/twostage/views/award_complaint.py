# -*- coding: utf-8 -*-
from openprocurement.tender.openua.views.award_complaint import TenderUaAwardComplaintResource
from openprocurement.api.utils import (
    json_view,
    opresource,
    context_unpack
)
from openprocurement.api.validation import (
    validate_complaint_data,
    validate_patch_complaint_data
)

@opresource(name='Tender Two Stage Award Complaints',
            collection_path='/tenders/{tender_id}/awards/{award_id}/complaints',
            path='/tenders/{tender_id}/awards/{award_id}/complaints/{complaint_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender TS award complaints")
class TenderTSAwardComplaintResource(TenderUaAwardComplaintResource):

    def complaints_len(self, tender):
        return sum([len(i.complaints) for i in tender.awards], sum([len(i.complaints) for i in tender.qualifications], len(tender.complaints)))

    @json_view(content_type="application/json", permission='create_award_complaint', validators=(validate_complaint_data))
    def collection_post(self):
        self.request.errors.add('body', 'data', 'Award Complaints not implemented')
        self.request.errors.status = 403
        return

    @json_view(content_type="application/json", permission='edit_complaint', validators=(validate_patch_complaint_data))
    def patch(self):
        self.request.errors.add('body', 'data', 'Award Complaints not implemented')
        self.request.errors.status = 403
        return
