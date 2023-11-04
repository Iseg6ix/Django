from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm
from .models import Student
from django.forms import formset_factory

def create_student(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['name']
            student = Student(name = student_name)
            student.save()
            return HttpResponse(f"Profile created successfully for {student_name}")
    form = CreateStudentForm()
    create_student_form_set = formset_factory(CreateStudentForm, extra=1)
    formset = create_student_form_set(
        initial = [
            {
                'name': 'Jude',
            }
        ]
    )
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'administration/create_student.html', context)
