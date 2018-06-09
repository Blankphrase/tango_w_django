from django.contrib import admin

# Registering each class for the Web Admin 
from django.contrib import admin
from rango.models import Category, Page

# to customise the Admin Interface 

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# creating a class to autopoplate Category Slug
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin) # registering the CategoryAdmin
admin.site.register(Page, PageAdmin) 
# register must be below the class, if the class exists. 