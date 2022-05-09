from django.urls import path
from . import views
#from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name="index"),
    path('createshorturl', views.createshorturl, name="createshorturl"),
    path("urlcreated", views.urlcreated, name="urlcreated"),
    path('<term>', views.shortredirect),
]
