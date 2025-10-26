from django.forms import forms
from .models import person
class PersonForm(forms.Form):
    class Meta:
        model = person
        __fields__= all
