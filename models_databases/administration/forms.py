from django import forms

class CreateStudentForm(forms.Form):
    name = forms.CharField(label='Student name', max_length=100)
    graduated = forms.BooleanField(required=False)
    bio = forms.CharField(label='Student Bio', max_length=1000, required=False, widget=forms.Textarea)   # Widget = forms.textarea attr give us more space to input text.
