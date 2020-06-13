from django import forms
from .models import Player

class PlayerDetailForm(forms.ModelForm):
    class Meta():
        model = Player
        fields=['first_name','last_name','image_uri','jersey_number','country','team']
