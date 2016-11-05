
from django.conf.urls import url
from .views import MovieViewSet, RatingViewSet

urlpatterns = [
    url(r'^movies/$', MovieViewSet.as_view({
    	'get': 'list', 'post':'create'})),
    url(r'^movies/(?P<pk>[0-9]+)/$', MovieViewSet.as_view({
    	'get': 'retrieve',
    	'delete':'destroy',
    	'patch':'update'})),
    url(r'^movies/(?P<movie>[0-9]+)/ratings/$',
        RatingViewSet.as_view({
        'get': 'list'})),
    url(r'^ratings/$',
        RatingViewSet.as_view({
        'post':'create'})),
    url(r'^movies/(?P<movie>[0-9]+)/ratings/(?P<pk>[0-9]+)/$',
        RatingViewSet.as_view({
        'get':'retrieve',
        'delete':'destroy',
        'patch':'update'})),
]
