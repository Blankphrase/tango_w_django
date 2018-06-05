from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from rango import views

# allows us to call the function url and point to the index view for the mapping in urlpatterns.
urlpatterns = [
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
