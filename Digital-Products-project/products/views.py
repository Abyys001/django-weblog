from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from rest_framework.views import APIView

from .models import Category, File, Product
from .serializer import CategorySerializer, FileSerializer, ProductSerializer


class ProductListView(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)