from django import forms
from .models import Data
from .models import User


class DataForm(forms.ModelForm):

    class Meta:

        model = Data
        fields = ('number_1', 'number_2',)

class UserForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ('sender', 'recipient', 'password', 'subject', 'text',)