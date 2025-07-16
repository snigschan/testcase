from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import NotificationPreference, CardDetail
from .serializers import NotificationPreferenceSerializer, CardDetailSerializer

# --- Notification Preference ViewSet ---
class NotificationPreferenceViewSet(viewsets.ModelViewSet):
    queryset = NotificationPreference.objects.all().order_by('-created_at')
    serializer_class = NotificationPreferenceSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = super().get_queryset()
        mobile = self.request.query_params.get('mobile_number')
        if mobile:
            queryset = queryset.filter(mobile_number=mobile)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.notification_tune:
            instance.notification_tune.delete(save=False)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Card Detail ViewSet ---
class CardDetailViewSet(viewsets.ModelViewSet):
    queryset = CardDetail.objects.all()
    serializer_class = CardDetailSerializer
