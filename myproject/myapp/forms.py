# myproject/myapp/forms.py
from django import forms
from .models import Entry
from django.contrib.auth.forms import UserCreationForm

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        help_text="Required. 20 characters or fewer. Letters and digits only.",
        error_messages={
            'invalid': 'This value may contain only letters and numbers.',
        }
    )