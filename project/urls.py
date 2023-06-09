"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robotcategoryList', views.RobotCategoryList.as_view()),
    path('robotcategoryUpdate/<int:pk>/', views.RobotCategoryUpdate.as_view()),
    path('manufacturerList', views.ManufacturerList.as_view()),
    path('manufactureUpdate/<int:pk>/', views.ManufacturerUpdate.as_view()),
    path('robotList', views.RobotList.as_view()),
    path('robotUpdate/<int:pk>/', views.RobotUpdate.as_view()),
    # path('api-root', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
