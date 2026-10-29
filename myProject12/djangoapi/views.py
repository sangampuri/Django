from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# @api_view(['GET'])
# def hello_api(request):
#     data = [
#     {'name': 'Ram', 'age': 20},
#     {'name': 'Sita', 'age': 22},
#     {'name': 'Hari', 'age': 21}
# ]
#     return Response(data)        

       
@api_view(['GET','POST'])
def hello_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    #!This is one way
    # data = []
    # for student in students:
    #     data.append(
    #         {
    #         'name': student.name,
    #         'email': student.email,
    #         'age': student.age
    #     }
    #     ) 

    #!This is other way
        # data=[
        #     {'name': student.name,
        #     'email': student.email,
        #     'age': student.age
        #     }
        # for student in students
        # ]

        # return Response(data)

    # elif request.method == 'POST':
        # name = request.data['name']
        # email = request.data['email']
        # age = request.data['age']

        # student = Student.objects.create(
        #     name = name,
        #     email = email,
        #     age = age,
        # )

        # return Response({
        #     'name': student.name,
        #     'email': student.email,
        #     'age': student.age
        # })

        
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.errors, status=400)


