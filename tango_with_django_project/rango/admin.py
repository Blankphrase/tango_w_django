from django.contrib import admin

# Registering each class for the Web Admin 
from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)