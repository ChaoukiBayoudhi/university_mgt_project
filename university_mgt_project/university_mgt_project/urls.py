"""
URL configuration for university_mgt_project (Django 6.1).

API surface lives under /api/ and is provided by student_app.urls
(DefaultRouter + custom @action routes).
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # REST API: /api/students/, /api/courses/, ... + custom actions
    path("api/", include("student_app.urls")),
]
