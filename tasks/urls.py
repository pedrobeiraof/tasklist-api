from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ListCreateTask.as_view()),
    path('<int:pk>', views.RetrieveUpdateTask.as_view()),
]
