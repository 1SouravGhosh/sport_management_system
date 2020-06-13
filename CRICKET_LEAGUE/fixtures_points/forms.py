from django import forms
from .models import Fixture

class TeamDetailForm(forms.ModelForm):
    class Meta():
        model = Fixture
        fields=['name','logo_uri','state']
