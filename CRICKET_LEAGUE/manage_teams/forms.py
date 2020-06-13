from django import forms
from .models import Team

class TeamDetailForm(forms.ModelForm):
    class Meta():
        model = Team
        fields=['name','logo_uri','state']
