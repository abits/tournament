from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.models import User
from models import Tournament, Team, Match, Bet
from django.forms.models import modelformset_factory, formset_factory
from django.shortcuts import render_to_response
from forms import BetForm
from django.core.context_processors import csrf
from datetime import datetime, timedelta


def show_teams(request):
    teams_list = Team.objects.all()
    template = loader.get_template('teams_list.html')
    context = Context({
        'teams_list': teams_list,
    })
    return HttpResponse(template.render(context))

def index(request):
    match_list = Match.objects.all().order_by('date')

    template = loader.get_template('match_list.html')
    context = Context({
        'match_list': match_list,
        })
    return HttpResponse(template.render(context))

def bet(request):
    context  = {}
    context.update(csrf(request))
    BetFormSet = formset_factory(BetForm, extra=0)
    if request.method == 'POST': # If the form has been submitted...
        formset = BetFormSet(request.POST)
        if formset.is_valid(): # All validation rules pass
            print formset.cleaned_data
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/matches') # Redirect after POST
    else:
        initial_data = []
        for match in Match.objects.filter(date__gt=datetime.now() - timedelta(minutes=15)):
            match_id = { 'match': match.pk }
            initial_data.append(match_id)
        print initial_data
        formset = BetFormSet(initial=initial_data) # An unbound form

    context['formset'] = formset
    return render_to_response('bet_list.html', context)


def init(request, scope):
    tournament = Tournament()
    if scope == 'all' or scope == 'matches':
        tournament.initialize_matches()
    if scope == 'all' or scope == 'teams':
        tournament.initialize_teams()
    return HttpResponse()

