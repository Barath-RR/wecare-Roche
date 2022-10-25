from django.urls import path
from django.views import View
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('landing/', views.landing, name='landing'),
    path('event/', views.event, name='event'),
    path('tracker/', views.tracker, name='tracker'),
    path('volunteer/', views.volunteering, name='volunt'),

    path('speaker/', views.map, name='speaker'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
