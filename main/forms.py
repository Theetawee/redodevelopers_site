from django import forms
from .models import HepB


class HepBForm(forms.ModelForm):
    class Meta:
        model = HepB
        fields = ['name', 'gender', 'phone', 'school', 'state']
    # Override the state field widget to use RadioSelect
    