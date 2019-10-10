from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', views.UserRegister.as_view(),name='user-register'),
    path('change-password/',views.UserChangePassWord.as_view(),name='user-change-password'),
    path('change-wbl-password/',views.ChangeWblPassword),
]