from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.base),
    url(r'^about_me', views.about_me), 
  
]