from django.db import models

class ActiveCarrierManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Carrier(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active_objects = ActiveCarrierManager()

    def __str__(self):
        return f"{self.name} ({self.code})"

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    tracking_number = models.CharField(max_length=50, unique=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.PROTECT, related_name='shipments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['tracking_number']),
            models.Index(fields=['status']),
        ]