from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>',views.UserDetail.as_view(),name='user-detail'),
    path('profiles/',views.ProfileList.as_view(),name='profile-list'),
    path('profiles/<int:pk>',views.ProfileDetail.as_view(),name='profile-detail'),
]