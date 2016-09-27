from django.shortcuts import render
from django.http import HttpResponse

def user_posts (request):

    context = {

    }

    # return HttpResponse("Here we be, you and I.")
    return render(request, "users/user_posts.html", context)
