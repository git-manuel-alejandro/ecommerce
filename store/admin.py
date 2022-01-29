from django.contrib import admin
from .import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display =  ('name','price', 'stock', 'category', 'modified_date','is_available')
    prepopulated_fields = {'slug' : ('name' , )}


admin.site.register(models.Product , ProductAdmin)