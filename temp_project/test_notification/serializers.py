from rest_framework import serializers
from .models import NotificationPreference, CardDetail

class NotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPreference
        fields = '__all__'

class CardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDetail
        fields = '__all__'
