from django.db import transaction
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from . import models, serializers, enums


class ListCreateTask(ListCreateAPIView):
    serializer_class = serializers.ListCreateTask
    queryset = models.Task.objects.filter(deleted_at__isnull=True).all()


class RetrieveUpdateTask(RetrieveUpdateAPIView):
    # serializer_class = serializers.RetrieveTask
    queryset = models.Task.objects.all()

    def perform_update(self, serializer):
        return super().perform_update(serializer)
