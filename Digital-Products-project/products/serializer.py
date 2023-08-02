# serializer file
from rest_framework import serializers

from .models import Category,Product,File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('titel', 'description', 'avatar')
 
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File 
        fields = ('title', 'file')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ('title', 'description', 'avatar', 'category')
