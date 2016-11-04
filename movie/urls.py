
from django.conf.urls import url
from .views import MovieViewSet, RatingViewSet

urlpatterns = [
    url(r'^movie/$', MovieViewSet.as_view({
    	'get': 'list', 'post':'create'})),
    url(r'^movie/(?P<pk>[0-9])/$', MovieViewSet.as_view({
    	'get': 'retrieve',
    	'delete':'destroy',
    	'patch':'update'})),
    url(r'^movie/(?P<movie>[0-9])/rating/$',
        RatingViewSet.as_view({
        'get': 'list'})),
    url(r'^rating/$',
        RatingViewSet.as_view({
        'post':'create'})),
]
