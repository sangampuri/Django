from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET','POST'])
def list_stu(request):
   if request.method == 'GET':
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)
      return Response(serializer.data)

   elif request.method == 'POST':
      serializer = StudentSerializer(data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)

@api_view(['PUT'])
def update_stu(request, student_id):
   student = get_object_or_404(Student, id = student_id)
   serializer = StudentSerializer(student, data=request.data)
   if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
   
   return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return Response(status=204)