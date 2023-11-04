from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm
from .models import Student


def create_student(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['name']
            student = Student(name = student_name)
            student.save()
            return HttpResponse(f"Profile created successfully for {student_name}")
    form = CreateStudentForm()
    context = {
        'form': form
    }
    return render(request, 'administration/create_student.html', context)
