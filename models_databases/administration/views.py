from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateStudentForm
from .models import Student
from django.forms import formset_factory, BaseFormSet


class BaseStudentFormset(BaseFormSet):
   def clean(self):
       if any(self.errors):
        return
       names = []
       for form in self.forms:
        if self.can_delete and self.should_delete_form(form):
           continue
        name = form.cleaned_data.get('name')
        if name in names:
           raise ValueError('Students in a set must have distinct names.')
        names.append(name)

def create_student(request):
    StudentFormset = formset_factory(CreateStudentForm, formset=BaseStudentFormset, can_order=2)
    if request.method == 'POST':
        student_formset = StudentFormset(request.POST)
        return HttpResponse(student_formset.cleaned_data)
    student_formset = StudentFormset(initial= [{'name': 'John'}, {'name': 'John'}])
    context = {
        'formset': student_formset
    }
    return render(request, 'administration/create_student.html', context)