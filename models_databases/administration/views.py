from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm
from .models import Student



def create_student(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['name']
            student = Student.objects.create(name=student_name)
            student.save()
            return HttpResponse(f"Account successfully created for {student_name}")
        else:
            form = CreateStudentForm()
    form = CreateStudentForm()
    return render(request, 'administration/create_student.html', {'form': form})