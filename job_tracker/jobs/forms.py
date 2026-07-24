from django import forms
from .models import JobApplication
from django.core.exceptions import ValidationError
from datetime import date

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'application_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary < 0:
            raise ValidationError('Salary cannot be negative.')
        return salary

    def clean(self):
        cleaned_data = super().clean()
        application_date = cleaned_data.get('application_date')
        deadline = cleaned_data.get('deadline')
        if application_date and deadline and deadline < application_date:
            raise ValidationError('Deadline cannot be earlier than application date.')
        return cleaned_data

    def clean_notes(self):
        notes = self.cleaned_data.get('notes')
        if notes and len(notes) > 500:
            raise ValidationError('Notes cannot exceed 500 characters.')
        return notes