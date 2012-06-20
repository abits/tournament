from django import forms
from matches.models import Bet
from django.contrib.auth.models import User

class ScoreWidget(forms.MultiWidget):
    def __init__(self, widgets, attrs=None):
        self.widgets = [isinstance(w, type) and w() or w for w in widgets]
        super(forms.MultiWidget, self).__init__(attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None, None]

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
    user = forms.ModelChoiceField(queryset=User.objects.all,
                                  widget=forms.HiddenInput)
    match = forms.ModelChoiceField(queryset=User.objects.all,
                                   widget=forms.HiddenInput)
    date_placed = forms.DateField(widget=forms.HiddenInput)
    active = forms.BooleanField(widget=forms.HiddenInput)
    score_1 = forms.IntegerField(min_value=0, max_value=99)
    score_2 = forms.IntegerField(min_value=0, max_value=99)
    score_1_widget = forms.TextInput(attrs={'size': 1, 'maxlength': 2})
    score_2_widget = forms.TextInput(attrs={'size': 1, 'maxlength': 2})
    score_widget = ScoreWidget(widgets=[score_1_widget, score_2_widget])
    result = forms.MultiValueField(fields=[score_1, score_2], widget=score_widget)



#        stake = models.CharField(max_length=128, blank=True)
#    result = models.CharField(max_length=8, blank=True)
#    users = models.ForeignKey(User)
#    match = models.ForeignKey(Match)
#    date_placed = models.DateTimeField(blank=True)
#    active = models.BooleanField(default=True)