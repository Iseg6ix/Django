from django import forms


class CreateStudentForm(forms.Form):
    name = forms.CharField(label= 'Student Name', max_length=100, required=True)
    graduate = forms.BooleanField(required=False)
    student_bio = forms.CharField(label='Student Bio', max_length=1000, required=False, widget=forms.Textarea)