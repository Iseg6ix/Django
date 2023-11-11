from django import forms


class CreateStudentForm(forms.Form):
    name = forms.CharField(label= 'Student Name', max_length=100, required=True)