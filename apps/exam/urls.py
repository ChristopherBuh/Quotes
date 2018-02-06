from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^quotes$', views.quotes),
    url(r'^createquote$', views.createquote),
    url(r'^logout$', views.logout),
    url(r'^favorite/(?P<quote_id>\d+)$', views.add_favquote),
    url(r'^remove_favorite/(?P<quote_id>\d+)$', views.rem_favquote),
    url(r'^users/(?P<user_id>\d+)$', views.display_user)

  ]