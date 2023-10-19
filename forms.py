from django import forms
from testapp.models import Student

class Studentform(forms.ModelForm):
    #fields for validation
    class Meta:
        model=Student
        fields='__all__'
