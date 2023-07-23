# path file for profile app

from django.urls import path

# from rest_framework.routers import DefaultRouter

from .views import page



urlpatterns = [
    path('page/', page)
]