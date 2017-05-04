from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),       # the index path goes to the personal page since it is the main thing of this project
    url(r'^redirect/$', views.redirect, name="redirect")    # when the person types in an address it gets redirected to a new page
]
