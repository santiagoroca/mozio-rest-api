from django.conf.urls import patterns, url

from mozioapp import views

urlpatterns = patterns('',
url(r'^provider/(?P<pk>[0-9]+)$', views.ProviderDetail.as_view()),
url(r'^provider$', views.ProviderList.as_view()),
url(r'^polygon$', views.PolygonDetail.as_view()),
url(r'^provider/(?P<pk>[0-9]+)/polygon$', views.PolygonList.as_view()),
url(r'^polygon/(?P<pk>[0-9]+)/point$', views.PointList.as_view()),
url(r'^point$', views.PointDetail.as_view()),)