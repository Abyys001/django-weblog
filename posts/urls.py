# Post URLs

from django.urls import path

# importing router
from rest_framework.routers import DefaultRouter

# My views
# from .views import PostListView , PostDetailView
from .views import PostView

# router object
router = DefaultRouter()

router.register(r'', PostView)



urlpatterns = router.urls