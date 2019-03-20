from django.db import transaction
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.utils import timezone
from . import models, serializers, enums


class ListCreateTaskView(ListCreateAPIView):
    serializer_class = serializers.ListCreateTask
    queryset = models.Task.objects.filter(deleted_at__isnull=True).all()
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'description')


class RetrieveUpdateTaskView(RetrieveUpdateAPIView):
    serializer_class = serializers.RetrieveTask
    queryset = models.Task.objects.all()


class UpdateTaskStatusView(APIView):

    def patch(self, request, pk):
        task = models.Task.objects.filter(id=pk).first()
        status_id = request.data.get('status', None)

        if (task and status_id
            and status_id in [str(status) for status in enums.TaskStatus.list()]):
                task.status_id = status_id
                task.save()
                return Response(status=200, data=model_to_dict(task))
        return Response(status=400)


class DeleteTaskView(APIView):

    def delete(self, request, pk):
        task = models.Task.objects.filter(id=pk).first()
        if task:
            task.deleted_at = timezone.now()
            task.save()
            return Response(status=200)
        return Response(status=404)
