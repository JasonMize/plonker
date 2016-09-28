from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm

def register (request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)

            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, "User created! Please login below.")

            return redirect ('accounts:login')

    else:
        form = RegistrationForm()

    context = {
        "form": form,
    }

    return render(request, 'accounts/register.html', context)

