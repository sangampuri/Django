from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_api(request):
    data = {
        'message': 'Hello, Django REST Framework!',
        'course':'Python + Django'
    }
    return Response(data)        

       


