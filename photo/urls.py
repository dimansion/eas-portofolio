from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
