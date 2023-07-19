# Post URLs

from django.urls import path

# My views
from .views import PostListView, PostDetailView

urlpatterns = [
    
    path('', PostListView.as_view(), name='post-detail'),

    path("<int:pk>/", PostDetailView.as_view(), name="post-detail")

]
