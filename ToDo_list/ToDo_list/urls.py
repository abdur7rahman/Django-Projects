"""
URL configuration for ToDo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Base_Py import views
# from Base_Py.views import LoginResponse, RegisterpageResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginResponse, name='login'),
    path('register/', views.RegisterpageResponse, name='register'),
    path('logout', views.LogoutResponse),
    path('', views.TaskListResponse, name='taskspage'),
    path('task/<int:id>/', views.TaskDetailResponse, name='detail'),
    path('task_create', views.TaskCreateResponse),
    path('task-update/<int:id>/', views.TaskUpdateResponse, name='update'),
    path('task-delete/<int:id>/', views.TaskDeleteResponse, name='delete'),
]
