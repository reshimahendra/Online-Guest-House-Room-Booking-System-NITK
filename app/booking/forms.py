from django import forms
from . models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class UserImageForm(forms.ModelForm):

    class Meta:
        model = ExtendedUser
        fields = [
            'image'
        ]


class TransactionForm(forms.Form):
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),required=False)
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),required=False)