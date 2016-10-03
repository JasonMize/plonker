from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Count
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post, Ripple
from .forms import CreatePostForm, CreateRippleForm



def user_posts (request, id=None):

    if id:
        user_name = User.objects.get(id = id)
    else: 
        user_name = request.user    
    posts = user_name.post_set.all()

    context = {
        'user_name' : user_name, 
        'posts' : posts,
    }

    # return HttpResponse("Here we be, you and I.")
    return render(request, "users/user_posts.html", context)




@login_required
def ripple(request, post_id):
    original_post = Post.objects.get(id=post_id)
  

    if request.method == "POST":
        form = CreateRippleForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user

            new_post.original_post = 'original_post'

            new_post.save()
            messages.success(request, "You Plonked a Ripple!")
            return redirect ('users:user_posts', request.user.pk)
    else:
        form = CreateRippleForm()

    context = {
        'form' : form, 
        'original_post' : original_post,  
    }

    return render (request, 'users/ripple.html', context)





def users_list(request):
    users_count = User.objects.count()
    posts_count = Post.objects.count()
    users = User.objects.all().order_by(Lower('username'))

    context = {
        'users' : users, 
        'users_count' : users_count,
        'posts_count' : posts_count, 
    }

    return render (request, 'users/users_list.html', context)



@login_required
def create_post (request):

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, "You Plonked!")
            return redirect ('users:user_posts', request.user.pk)
    else:
        form = CreatePostForm()

    context = {
        'form' : form, 
    }

    return render (request, 'users/create_post.html', context)








