from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#! Creating the registration view

# def register(request):
#     form = UserCreationForm() #This creates a new, blank registration form.
#     return render(request, 'accounts/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # This gets the data entered in thr form.

        if form.is_valid():
            form.save()
            return render(request,'accounts/register_success.html')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'accounts/home.html',{'username': request.user.username})
