"""
URL configuration for tax_calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from tax.views import default_view, calculate_total, tax_rate_view

urlpatterns = [
    path('', default_view, name='default_view'),
    re_path(r'^(?P<price>(\d+(\.\d{2})?)|(\.\d{2}))/$', calculate_total, name='calculate_total'),
    path('taxrate/', tax_rate_view, name='tax_rate_view'),
    path('admin/', admin.site.urls),
]