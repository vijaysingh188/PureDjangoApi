from django import forms
from . models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_sal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal < 10000:
            raise forms.ValidationError('minimum salary should be 10000 ')
        return inputsal


    class Meta:
        model = Employee
        fields = '__all__'

