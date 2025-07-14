from django import forms
from core.models import LeaveRequest



class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = '__all__'

    def clean_employee(self):
        employee = self.cleaned_data.get('employee')
        if not employee:
            raise forms.ValidationError("Поле 'Employee' є обов'язковим. Будь ласка, виберіть працівника.")
        return employee

    def clean(self):
        cleaned_data = super().clean()
        sick_days = cleaned_data.get('sick_days')
        holiday_days = cleaned_data.get('holiday_days')

        if sick_days is not None and sick_days > 5:
            raise forms.ValidationError("Кількість лікарняних днів не може перевищувати 5.")

        if holiday_days is not None and holiday_days > 3:
            raise forms.ValidationError("Кількість днів відпочинку не може перевищувати 3.")

        return cleaned_data