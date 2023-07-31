from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    parent = models.ForeignKey("self", verbose_name=_("parent"), on_delete=models.CASCADE)

    title = models.CharField(_('title'), max_length=50)

    description = models.TextField(_('description'), blank=True)

    avatar = models.ImageField(_("avatar"), upload_to='avatar/categorys/')

    is_enable = models.BooleanField(_('is enable'), default=True)

    created_time = models.DateTimeField(_('created time'), auto_now_add=True)

    updated_time = models.TimeField(_('updated time'), auto_now=True)
    
    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):

    category = models.ManyToManyField("products.Category", verbose_name=_("category"))

    title = models.CharField(_('title'), max_length=50)

    description = models.TextField(_('description'), blank=True)

    avatar = models.ImageField(_("avatar"), upload_to='avatar/products/')

    is_enable = models.BooleanField(_('is enable'), default=True)

    created_time = models.DateTimeField(_('created time'), auto_now_add=True)

    updated_time = models.TimeField(_('updated time'), auto_now=True)
    
    class Meta:
        db_table = 'Products'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class File(models.Model):

    product = models.ForeignKey("products.Product", verbose_name=_("product"), on_delete=models.CASCADE)

    file = models.FileField(_("file"), upload_to="file/%Y/%M/%D/")

    title = models.CharField(_('title'), max_length=50)

    description = models.TextField(_('description'), blank=True)

    avatar = models.ImageField(_("avatar"), upload_to='avatar/files/')

    is_enable = models.BooleanField(_('is enable'), default=True)

    created_time = models.DateTimeField(_('created time'), auto_now_add=True)

    updated_time = models.TimeField(_('updated time'), auto_now=True)
    
    class Meta:
        db_table = 'Files'
        managed = True
        verbose_name = 'File'
        verbose_name_plural = 'Files'
