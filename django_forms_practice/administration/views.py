from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm
from .models import Student
from django.forms import formset_factory

def create_student(request):
    StudentFormSet = formset_factory(CreateStudentForm)
    student_formset = StudentFormSet(initial=[{'name': 'John'}, {'name': "John"}])
    if request.method == 'POST':
        student_formset = StudentFormSet(request.post)
        if student_formset.is_valid():
            return HttpResponse(student_formset.cleaned_data)
    context = {
        'formset': student_formset
    }
    return render(request, 'administration/create_student.html', context)
