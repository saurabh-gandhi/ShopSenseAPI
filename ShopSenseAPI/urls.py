from django.conf.urls import include, url
from django.contrib import admin
from Movies import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'ShopSenseAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/', views.MovieView.as_view())
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
