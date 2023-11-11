from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm
from .models import Student
from django.forms import formset_factory, BaseFormSet


def create_student(request):
    StudentFormSet = formset_factory(CreateStudentForm)
    student_form = StudentFormSet(initial = [{'name': 'John'}])
    if request.method == 'POST':
        form = student_form(request.POST)
        return HttpResponse(form.cleaned_data)
    context = {
        'formset': student_form,
    }
    return render(request, 'administration/create_student.html', context)
