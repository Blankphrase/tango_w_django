import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    #First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories. # This might seem a little bit confusing, but it allows us to iterate # through each data structure, and add the data to our models.
    python_cat = add_cat('Python', views=128, likes=64)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        views=50)

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=40)
        
    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=38)
    
    django_cat = add_cat('Django', views=64, likes=32)
    
    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
        views=24)
    
    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=18)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=22)
    
    frame_cat = add_cat('Other Frameworks', views=32, likes=16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=14)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=18)

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    # print out the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(" - {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    # 'get_or_create' used to check if entry exists in the DB, if it doesn't the method creates.
    p.save()
    return p

#Python cat = V128/L64
#Django cat = V64/L32
#Other cat = V32/L16

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()

"""
The __name__ == '__main__' trick is a useful one that allows a Python module to act as either
a reusable module or a standalone Python script. 
Consider a reusable module as one that can be imported into other 
modules (e.g. through an import statement), while a standalone Python script 
would be executed from a terminal/Command Prompt by entering python module.py.
"""