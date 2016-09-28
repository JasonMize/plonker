from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .forms import LoginForm
from . import views

urlpatterns = [

    url (r'^register/$',
        views.register, 
        name='register'),

    url (r'^login/$', 
        login,
        {'authentication_form': LoginForm},
        name='login'),
    
    url (r'^logout/$',
        logout, 
        {'template_name': 'accounts/logout.html'},
        name='logout'),
]







