from django.shortcuts import render, get_object_or_404

from users.models import Post

def index(request):

    posts = Post.objects.all()
    fred = "blue"

    context = {
        'fred': fred,
        'posts':posts,
    }

    return render (request, "core/index.html", context)



