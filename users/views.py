from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Count
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Post
from .forms import CreatePostForm
from django.contrib.auth.models import User



def user_posts (request, id=None):

    if id:
        posts = Post.objects.filter(user_id = id)
    else: 
        posts = Post.objects.filter(user = request.user)

    context = {
        'posts' : posts,
    }

    # return HttpResponse("Here we be, you and I.")
    return render(request, "users/user_posts.html", context)






def users_list(request):
    users_count = User.objects.count()
    posts_count = Post.objects.count()
    users = User.objects.all().order_by(Lower('username'))

    context = {
        'users' : users, 
        'users_count' : users_count,
        'posts_count' : posts_count, 
    }

    return render (request, "users/users_list.html", context)







def create_post (request):

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_id = request.user.pk
            new_post.save()
            messages.success(request, "You Plonked!")
            return redirect ('users:user_posts', request.user)
    else:
        form = CreatePostForm()

    context = {
        'form' : form, 
    }

    return render (request, 'users/create_post.html', context)






