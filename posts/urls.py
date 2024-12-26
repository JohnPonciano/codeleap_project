# careers/urls.py

from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),  # GET to list posts and POST to create a post
    path('<int:id>/', PostDetailView.as_view(), name='post-detail'),  # PATCH or DELETE to update or delete a post
]
