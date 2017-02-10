# -*- coding: utf-8 -*-
from openprocurement.tender.openua.views.lot import TenderUaLotResource as TenderLotResource

from openprocurement.api.utils import (
    save_tender,
    opresource,
    json_view,
    context_unpack,
    get_now,
    calculate_business_date
)
from openprocurement.api.validation import (
    validate_lot_data,
)
from openprocurement.tender.twostage.models import TENDERING_EXTRA_PERIOD


@opresource(name='Tender Two Stage Lots',
            collection_path='/tenders/{tender_id}/lots',
            path='/tenders/{tender_id}/lots/{lot_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender Two Stage lots")
class TenderTSLotResource(TenderLotResource):
    def validate_update_tender(self, operation):
        tender = self.request.validated['tender']
        if tender.status not in ['active.tendering']:
            self.request.errors.add('body', 'data', 'Can\'t {} lot in current ({}) tender status'.format(operation, tender.status))
            self.request.errors.status = 403
            return
        if calculate_business_date(get_now(), TENDERING_EXTRA_PERIOD, tender) > tender.tenderPeriod.endDate:
            self.request.errors.add('body', 'data', 'tenderPeriod should be extended by {0.days} days'.format(TENDERING_EXTRA_PERIOD))
            self.request.errors.status = 403
            return
        return True

    @json_view(content_type="application/json", validators=(validate_lot_data,), permission='edit_tender')
    def collection_post(self):
        """Add a lot
        """
        if not self.validate_update_tender('add'):
            return
        lot = self.request.validated['lot']
        lot.date = get_now()
        tender = self.request.validated['tender']
        tender.lots.append(lot)
        if self.request.authenticated_role == 'tender_owner':
            tender.invalidate_bids_data()
        if save_tender(self.request):
            self.LOGGER.info('Created tender lot {}'.format(lot.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'tender_lot_create'}, {'lot_id': lot.id}))
            self.request.response.status = 201
            self.request.response.headers['Location'] = self.request.route_url('Tender Two Stage Lots', tender_id=tender.id, lot_id=lot.id)
            return {'data': lot.serialize("view")}
