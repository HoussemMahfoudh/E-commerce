from django.contrib import admin
from .models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    prepopulated_fields = {'slug':('name',)}  #using prepopulated_fields attribute to specify fields where the value is automatically set using the value of another field

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nameProd', 'slug', 'price', 'stock','available','created_at','updated_at','Category']
    list_filter = ['available','created_at','updated_at']
    list_editable = ['price', 'stock', 'available']   #we use list_editable attribute in the ProductAdmin class to set the fields that can be edited from the list display page of our django administration site.
    prepopulated_fields = {'slug': ('nameProd',)}

admin.site.register(Product, ProductAdmin)


