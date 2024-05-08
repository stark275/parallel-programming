from django.urls import re_path, path
from . import views

app_name = 'concours' 
urlpatterns = [
    # ex: /concours/
    path("", views.index, name="index"),
    path("evaluate/", views.evaluate, name="evaluate"),
    path("get-task-result/<str:task_id>/", views.get_task_result, name="get_task_result"),
]