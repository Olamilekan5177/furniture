# user/views.py
from django.shortcuts import render, redirect
from.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            # Log the user in immediately
            login(request, user)
            # Redirect to a page, e.g., the profile page or homepage
            return redirect('in')  # Change 'profile' to whatever view you want to redirect to
    else:
        form = RegistrationForm()

    return render(request, 'user/signup.html', {'form': form})





@login_required
def profile(request):
    return render(request, 'user/profile.html')

