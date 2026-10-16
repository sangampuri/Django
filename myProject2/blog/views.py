from django.http import HttpResponse

def userid(request, user_id):
    return HttpResponse(f"Your user ID is: {user_id}")

def profile(request, user_name):
    return HttpResponse(f"Your user name is: {user_name}")