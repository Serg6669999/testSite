from django import forms
from .models import Data


class DataForm(forms.ModelForm):

    class Meta:

        model = Data
        fields = ('number_1', 'number_2',)