"""mysql_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path, re_path
from mysql_django import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/create', views.employee_create, name='emp_create'),
    path('employee/read', views.employee_read, name='emp_read'),
    path('employee/Search', views.employee_seach),
    path('employee/edit', views.employee_edit, name='emp_edit'),
    path('employee/updata/<int:id>/', views.employee_updata, name='emp_updata'),
    path('employee/delete/<int:id>/', views.employee_delete, name='emp_delete'),
    path('employee/login', views.employee_login),
    re_path(r'pagintation/prev-next/(?P<pg>\d*/?)', views.pagination_pvnx, name='pg_pvnx'),
    re_path(r'pagintation/prev-number/(?P<pg>\d*/?)', views.pagination_number, name='pg_num')
]
