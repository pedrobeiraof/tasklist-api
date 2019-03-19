from rest_framework import serializers
from . import models, enums


class ListCreateTask(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = ('id', 'title', 'description', 'status', 'updated_at')
        depth = 2

    updated_at = serializers.DateTimeField(format='%d/%m/%y %H:%M:%S', read_only=True)

    def create(self, validated_data):
        validated_data['status_id'] = enums.TaskStatus.TO_DO
        return super().create(validated_data)


class RetrieveTask(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = ('title', 'description')
