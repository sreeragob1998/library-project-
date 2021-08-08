from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AddNewLibrary,
    LibraryDetailView,
    LibraryUpdateView,
    LibraryDeleteView,
    LibraryListView,
    PostListAdminView,
    PostApproveView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/approve/', PostApproveView.as_view(), name='post-approve'),
    path('post-list-admin', PostListAdminView.as_view(), name='post-list-admin'),
    path('about/', views.about, name='blog-about'),

    path('library/new/', AddNewLibrary.as_view(), name='library-create'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('library/<int:pk>/update/', LibraryUpdateView.as_view(), name='library-update'),
    path('library/<int:pk>/delete/', LibraryDeleteView.as_view(), name='library-delete'),
    path('library-list', LibraryListView.as_view(), name='library-list'),

]
