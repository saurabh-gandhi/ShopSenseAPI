from django.conf.urls import include, url
from django.contrib import admin

from movies.service_apis.movie_list import MovieList
from movies.service_apis.movie_search_by_director import MovieSearchByDirector
from movies.service_apis.movie_search_by_genre import MovieSearchByGenre
from movies.service_apis.movie_search_by_title import MovieSearchByTitle
from movies.service_apis.userdetail import UserDetail
from movies.service_apis.userlist import UserList


urlpatterns = [
    url(r'^$', MovieList.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),

]

urlpatterns += [
    url(r'^search/director/(?P<director>[A-Za-z ]+)/$',
        MovieSearchByDirector.as_view()),
    url(r'^search/title/(?P<title>[A-Za-z :.-]+)/$',
        MovieSearchByTitle.as_view()),
    url(r'^search/genre/(?P<genre>[A-Za-z ]+)/$',
        MovieSearchByGenre.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
