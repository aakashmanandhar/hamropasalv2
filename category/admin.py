from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_on', 'updated_on', )
    list_filter = ('name', )
    fields = ('name', )
    search_fields = ('name', )

admin.site.register(Category, CategoryAdmin)
