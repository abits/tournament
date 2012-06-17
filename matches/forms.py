from django import forms
from matches.models import Match
from datetime import datetime, timedelta


class BetForm(forms.Form):

    score_1 = forms.IntegerField(required=False,
                                 min_value=0,
                                 max_value=99,
                                 widget=forms.TextInput(attrs={'class':'special'}))
    score_2 = forms.IntegerField(required=False,
                                 min_value=0,
                                 max_value=99,
                                 widget=forms.TextInput(attrs={'class':'special'}))
    match = forms.ModelChoiceField(widget=forms.HiddenInput, required=True, empty_label=None, queryset=Match.objects.filter(date__gt=(datetime.now() - timedelta(minutes=15))))