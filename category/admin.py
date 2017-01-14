from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_on', 'updated_on', 'category_id' )
    list_filter = ('name', )
    fields = ('name', 'category_id')
    search_fields = ('name', )

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'updated_on', 'category', )

admin.site.register(Product, ProductAdmin)
