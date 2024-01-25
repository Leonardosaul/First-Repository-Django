from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('hello/',views.hello,name="hello"),
    path('projects/',views.project,name="projects"),
    path('tasks/',views.tasks,name="tasks"),
    path('create_task/',views.createTask,name="create_task"),
    path('create_project/',views.createProject,name="create_project")
]