from rest_framework import serializers
from . import models


class ListTask(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = (
            'title',
            'description',
            'status',
            'updated_at'
        )
        depth = 2

    updated_at = serializers.DateTimeField(format='%d/%m/%y %H:%M:%S')
