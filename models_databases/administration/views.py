from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm, StudentModelForm, StudentModelFormNew
from django.forms import modelform_factory
from .models import Student


def create_student(request):
    student = Student.objects.get(age=12)
    if request.method == 'POST':
        student_form = StudentModelFormNew(request.POST, instance=student)
        student_form.save()
        return HttpResponse(f"Student was created")
    StudentModelFormFactory = modelform_factory(Student, fields='__all__')
    student_form = StudentModelFormFactory()
    
    context = {
        'form': student_form
    }
    return render(request, 'administration/create_student.html', context)