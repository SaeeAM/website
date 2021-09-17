"""satyam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from dashboard import views
from dashboard.views import (
    ServiceCreateView,
    DocumentCreateView,
    CostumerCreateView,
    ServiceDetail

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('track/', views.track, name='track'),
    path('search/', views.search, name='search'),
    path('Service/form/', ServiceCreateView.as_view(), name='service'),
    path('document/form/', DocumentCreateView.as_view(), name='document'),
    path('Costumer/form/', CostumerCreateView.as_view(), name='costumer'),
    path('<int:pk>/', ServiceDetail.as_view(), name='detail')
]
