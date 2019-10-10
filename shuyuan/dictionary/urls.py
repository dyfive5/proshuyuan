from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
# Create a router and register our viewsets with it.

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('words/', views.word_list,name='word-list'),
    path('words/<int:pk>',views.word_detial,name='word-detail'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>',views.UserDetail.as_view(),name='user-detail'),
    path('wordtypes/',views.WordTypeList.as_view(),name='word-type-list'),
    path('wordtypes/<int:pk>',views.WordTypeDetail.as_view(),name='word-type-detail'),
    path('likeword/<int:pk>',views.LikeWord,name='like-word'),
    path('dislikeword/<int:pk>',views.DislikeWord,name='dislike-word'),
]
urlpatterns = format_suffix_patterns(urlpatterns)