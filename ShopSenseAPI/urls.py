from django.conf.urls import include, url
from django.contrib import admin
from movies import views
urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/', views.MovieView.as_view())
]

urlpatterns += [
    url(r'^search/director/(?P<director>[A-Za-z ]+)/$',
        views.MovieSearchByDirector.as_view()),
    url(r'^search/title/(?P<title>[A-Za-z ]+)/$',
        views.MovieSearchByTitle.as_view()),
    url(r'^search/genre/(?P<genre>[A-Za-z ]+)/$',
        views.MovieSearchByGenre.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
