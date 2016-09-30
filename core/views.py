from django.shortcuts import render, get_object_or_404

from users.models import Post

def index(request):

    posts = Post.objects.all()

    context = {
        'posts':posts,
    }

    return render (request, "core/index.html", context)



