from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<domain>[a-z0-9]+(-[a-z0-9]+)*\.+[a-z]{2,})/$',
        views.search)
]
