
from django.conf.urls import url
from .views import MovieViewSet

movie_list = MovieViewSet.as_view({'get': 'list', 'post':'create'})
movie_detail = MovieViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    url(r'^movie/$', movie_list),
    url(r'^movie/(?P<pk>[0-9])/$', movie_detail),
]
