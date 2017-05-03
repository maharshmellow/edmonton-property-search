from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.index, name="index")       # the index path goes to the personal page since it is the main thing of this project
]
