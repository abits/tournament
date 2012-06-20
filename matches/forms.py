from django import forms
from matches.models import Match, Bet
from datetime import datetime, timedelta


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet