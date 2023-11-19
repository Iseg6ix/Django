from django import forms
from .models import Student

class CreateStudentForm(forms.Form):
    name = forms.CharField(label='Student name', max_length=100)
    



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []  # The exclude option can also be used, or fields = '__all__' to render all the fields.



class StudentModelFormNew(StudentModelForm):
    class Meta(StudentModelForm.Meta):
        exclude = ['graduated']