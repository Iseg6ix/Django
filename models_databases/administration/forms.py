from django import forms
from .models import Student

class CreateStudentForm(forms.Form):
    name = forms.CharField(label='Student name', max_length=100)
    



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'graduated']