
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello, welcome to my Shop!")

def products(request):
    return HttpResponse("This is the products page of my Shop.")