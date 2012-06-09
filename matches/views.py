from django.http import HttpResponse
from django.template import Context, loader
from models import Tournament, Team, Match

def show_teams(request):
    teams_list = Team.objects.all()
    template = loader.get_template('teams_list.html')
    context = Context({
        'teams_list': teams_list,
    })
    return HttpResponse(template.render(context))

def index(request):
    match_list = Match.objects.all()
    template = loader.get_template('match_list.html')
    context = Context({
        'match_list': match_list,
        })
    return HttpResponse(template.render(context))

def init(request, scope):
    tournament = Tournament()
    if scope == 'all' or scope == 'matches':
        tournament.initialize_matches()
    if scope == 'all' or scope == 'teams':
        tournament.initialize_teams()
    return HttpResponse()

