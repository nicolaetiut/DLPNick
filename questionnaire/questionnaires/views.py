from django.http import HttpResponse
from questionnaires.models import Questionnaire
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    latest_quests = Questionnaire.objects.all().order_by('creation_date')[:5]
    return render_to_response('index.html', {'latest_quests': latest_quests})

def results(request, quest_id):
    return HttpResponse("You're looking at the results of poll %s." % quest_id)

def start(request, quest_id):
    q = get_object_or_404(Questionnaire, pk=quest_id)
    return render_to_response('start.html', {'quest': q}, context_instance=RequestContext(request))

def go_to_page(request, quest_id, page_id):
    q = get_object_or_404(Questionnaire, pk=quest_id)
    current_q = request.session["current_quest_id"]
    current_p = request.session["current_page_id"]
    if current_q == quest_id:
        if current_p == page_id - 1:
            request.session["current_page_id"] = page_id
        else:
            return render_to_response('page.html', {'quest': q, 'page_id': current_p}, context_instance=RequestContext(request)) 
    else:
        request.session["current_quest_id"] = quest_id
    
    return render_to_response('page.html', {'quest': q, 'page_id': page_id}, context_instance=RequestContext(request))        

 
    