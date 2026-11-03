"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from jobs.views import (
    AddJobView,
    GetAllJobsView,
    GetOneJobView,
    UpdateJobView,
    DeleteJobView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addjob/', AddJobView.as_view()),
    path('getjobs/', GetAllJobsView.as_view()),
    path('getonejob/', GetOneJobView.as_view()),
    path('updatejob/', UpdateJobView.as_view()),
    path('deletejob/', DeleteJobView.as_view()),
]