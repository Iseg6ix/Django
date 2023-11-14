from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm, StudentModelForm
from .models import Student


def create_student(request):
    student_form = StudentModelForm()
    context = {
        'form': student_form
    }
    return render(request, 'administration/create_student.html', context)