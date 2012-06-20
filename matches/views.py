from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context, loader
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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    print request.user.pk

    context = RequestContext(request=request)
    BetFormSet = formset_factory(BetForm, extra=0)
    if request.method == 'POST':
        formset = BetFormSet(request.POST)
        if formset.is_valid():
            print formset.cleaned_data
            # Process the data in form.cleaned_data

            return HttpResponseRedirect('/matches')
    else:
        initial_data = []
        for match in Match.objects.filter(date__gt=datetime.now() - timedelta(minutes=15)):
            data = { 'match': match.pk, 'user': request.user.pk }
            initial_data.append(data)
        print initial_data

        formset = BetFormSet(initial=initial_data)

    context['formset'] = formset
    return render_to_response('bet_list.html', context)


def init(request, scope):
    tournament = Tournament()
    if scope == 'all' or scope == 'matches':
        tournament.initialize_matches()
    if scope == 'all' or scope == 'teams':
        tournament.initialize_teams()
    return HttpResponse()

