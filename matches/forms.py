from django import forms
from matches.models import Match, Bet
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet

    stake = forms.CharField(widget=forms.HiddenInput)
    user = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=User.objects.all())
    match = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Match.objects.all())
    date_placed = forms.DateField(widget=forms.HiddenInput)
    score_1 = forms.CharField(widget=forms.TextInput(attrs={'size': 1}))
    score_2 = forms.CharField(widget=forms.TextInput(attrs={'size': 1}))