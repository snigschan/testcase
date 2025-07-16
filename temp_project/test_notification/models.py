# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import Sum
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .storage_backends import SupabaseStorage
import logging
from decimal import Decimal


logger = logging.getLogger(__name__)


    

class NotificationPreference(models.Model):
    mobile_number = models.CharField(
        max_length=15,
        help_text="Mobile number to receive notifications (e.g., +971501234567)"
    )
    notification_tune = models.FileField(
        upload_to='notification_sounds/',
        help_text="Upload a custom notification sound (MP3, WAV, etc.)",
        null=True,
        blank=True
    )
    notification_duration = models.PositiveIntegerField(
        default=5,
        help_text="Duration (in seconds) to play the notification sound"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last updated timestamp")

    def __str__(self):
        return f"{self.mobile_number} - {self.notification_tune.name if self.notification_tune else 'No Tune'}"


class CardDetail(models.Model):
    cardholder_name = models.CharField(max_length=100)
    last4 = models.CharField(max_length=4, help_text="Last 4 digits of the card number")
    card_type = models.CharField(max_length=20, choices=[
        ('Visa', 'Visa'),
        ('Mastercard', 'Mastercard'),
        ('Amex', 'American Express'),
        ('Other', 'Other'),
    ])
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    card_token = models.CharField(max_length=255, help_text="Token from payment gateway", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"{self.card_type} ending in {self.last4}"

