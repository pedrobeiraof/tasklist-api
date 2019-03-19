from django.db import transaction
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from . import models, serializers


class ListCreateTask(ListCreateAPIView):
    serializer_class = serializers.ListTask
    queryset = models.Task.objects.filter(deleted_at__isnull=True).all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RetrieveUpdateTask(RetrieveUpdateAPIView):
    # serializer_class = serializers.RetrieveTask
    queryset = models.Task.objects.all()

    def perform_update(self, serializer):
        return super().perform_update(serializer)
