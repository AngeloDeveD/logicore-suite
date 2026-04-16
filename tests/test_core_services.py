import pytest
from apps.core_platform.shipments.services import ShipmentService

@pytest.mark.django_db
class TestShipmentService:
    def test_create_shipment_success(self, carrier):
        data = {
            "tracking_number": "TRK-12345",
            "carrier": carrier,
            "origin": "New York",
            "destination": "London"
        }
        shipment = ShipmentService.create_shipment(data)
        
        assert shipment.id is not None
        assert shipment.status == 'PENDING'
        assert shipment.carrier.code == "GEXP"

    def test_status_update_logic(self, carrier):
        data = {"tracking_number": "TRK-999", "carrier": carrier}
        shipment = ShipmentService.create_shipment(data)
        
        event = ShipmentService.update_status(shipment.id, "IN_TRANSIT")
        assert event.new_status == "IN_TRANSIT"
        assert event.shipment_id == shipment.id