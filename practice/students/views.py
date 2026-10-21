from django.shortcuts import render,get_object_or_404
from .forms import StudentForm
from django.shortcuts import redirect
from .models import Student

def create_student(request):
    if request.method == 'POST':
         form = StudentForm(request.POST) #Creates a form populated with the submitted data, ready for validation.

         if form.is_valid:
            form.save()
    else:   
        form = StudentForm() #Creates a empty form
    return render(request,'students/student_form.html', {'form':form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',{'students':students})

def update_student(request, student_id):
    student = get_object_or_404(Student, id = student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid:
            form.save()

            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request,'students/student_form.html',{'form':form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'students/student_confirm_delete.html',
        {'student': student}
    )