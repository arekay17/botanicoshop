from django.urls import path
from . import views
from django.conf.urls import url
from django.views import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
]

media_url = url(r'media/(?P<path>.*)', static.serve, {'document_root' : settings.MEDIA_ROOT}, name="media_folder")

if settings.DEBUG:
    urlpatterns.append(media_url)
    #urlpatterns.append(url_404)