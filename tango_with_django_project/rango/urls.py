from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from rango import views

# allows us to call the function url and point to the index view for the mapping in urlpatterns.
#regex '[\w\-]+' will look for any sequence of alphanumeric char. or numbers,
# and hypens (-), denoted: '\-' 
# match any denoted by the expression '[ ]' 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', views.index, name='rango'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
