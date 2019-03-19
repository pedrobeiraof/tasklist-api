from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ListCreateTaskView.as_view()),
    path('<int:pk>', views.RetrieveUpdateTaskView.as_view()),
    path('<int:pk>/update-status', views.UpdateTaskStatusView.as_view()),
]
