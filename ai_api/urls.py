from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/api/", views.handle, name="handle"),
    path("docs/", views.docs, name="documentation"),
    path("create/", views.createapi, name="createapi"),
]