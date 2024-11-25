# user/views.py
from django.shortcuts import render, redirect
from.forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save() #save the new user
           return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/signup.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'user/profile.html')

