from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    serviceDetailView,
    DataformCreateView,
    JoinusCreateView,
    ServiceListView,

)
from . import views

urlpatterns = [
    path('project/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.home, name='index'),
    path('search/', views.search, name='search'),
    path('service/', ServiceListView.as_view(), name='service'),
    path('service/<int:pk>/', serviceDetailView.as_view(), name='service-detail'),
    path('service/form/', DataformCreateView.as_view(), name='service-form'),
    path('JoinUs/', JoinusCreateView.as_view(), name='join'),
]
