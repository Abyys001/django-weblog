from django.contrib import admin

from .models import Product,Category,File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'updated_time']
    list_filter = ['is_enable']
    search_fields = ['title']



class FileAdminInline(admin.StackedInline):
    model = File
    fields = ['title', 'file']
    extra = 0



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "is_enable", "updated_time"]
    list_filter = ['category']
    filter_horizontal = ['category']
    search_fields = ['titel']
    inlines = [FileAdminInline]


