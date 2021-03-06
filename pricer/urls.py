from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"), 
    url(r'^redirect/$', views.redirect, name="redirect"),    # when the person types in an address it gets redirected to a new page
    url(r'^addresses/$', views.addresses, name="addresses")
]
