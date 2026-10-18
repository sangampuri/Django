from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def contact_form(request):
    return render(request,'contact.html')

def submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            Contact.objects.create(name=name, message=message)
            return HttpResponse("Thank you for your message!")
        else:
            return HttpResponse("Please fill in all fields.")
    return redirect('contact_form')
