from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def user_posts (request):

    posts = Post.objects.filter(user = request.user)

    context = {
        'posts':posts,
    }

    # return HttpResponse("Here we be, you and I.")
    return render(request, "users/user_posts.html", context)
