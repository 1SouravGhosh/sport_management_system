from django import forms
from .models import Fixture,Group


class FixtureDetailForm(forms.ModelForm):
    class Meta():
        model = Fixture
        fields=['team1','team2','group','completed']
        readonly_fields = ['date']
        widgets = {
                    'date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
                  }

class GroupDetailForm(forms.ModelForm):
    class Meta():
        model = Group
        fields=['name']
