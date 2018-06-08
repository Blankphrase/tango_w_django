from django.contrib import admin

# Registering each class for the Web Admin 
from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin) 
# register must be below the class, if the class exists. 