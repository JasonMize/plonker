from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_posts, name='user_posts'),
]