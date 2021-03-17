from django.urls import re_path
from django.contrib import admin

# Django 2.0+
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
]