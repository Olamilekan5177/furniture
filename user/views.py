# user/views.py
from django.shortcuts import render, redirect
from.forms import RegistrationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in immediately
            return redirect('profile')  # Redirect to profile or another page after login
    else:
        form = RegistrationForm()
    return render(request, 'user/signup.html', {'form': form})




@login_required
def profile(request):
    return render(request, 'user/profile.html')

