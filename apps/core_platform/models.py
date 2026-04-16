from django.db import models

class Carrier(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

class Shipment(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)