from rest_framework import serializers
from .models import Shipment, Carrier

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    carrier_info = CarrierSerializer(source='carrier', read_only=True)

    class Meta:
        model = Shipment
        fields = ['id', 'tracking_number', 'carrier', 'carrier_info', 'status', 'origin', 'destination', 'created_at']