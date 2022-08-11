from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class ProductAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = ProductAdminForm
    save_on_top = True
    list_display = ('title','category','get_image','price','available')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views',)

    def get_image(self,obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}"width="50">')
        return '-'

    get_image.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
