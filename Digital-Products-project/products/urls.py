from django.urls import path

from .views import ProductListView

urlpatterns = [
    path('products-list/', ProductListView.as_view()),
]
