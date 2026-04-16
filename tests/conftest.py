import pytest
from apps.core_platform.shipments.models import Carrier

@pytest.fixture
def carrier(db):
    return Carrier.objects.create(name="Global Express", code="GEXP")