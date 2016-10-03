from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_posts, name='user_posts'),
    url(r'^(?P<id>\d+)/$', views.user_posts, name='user_posts'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^users_list/$', views.users_list, name="users_list"),
    url(r'^ripple(?P<post_id>\d+)/$', views.ripple, name="ripple"),
]


