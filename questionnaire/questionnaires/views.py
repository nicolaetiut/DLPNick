from django.http import HttpResponse, HttpResponseRedirect
from questionnaires.models import Questionnaire, Question, Answer
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import quest_algorithm


def index(request):
    latest_quests = Questionnaire.objects.all().order_by('creation_date')[:5]
    return render_to_response('index.html', {'latest_quests': latest_quests})


def results(request, quest_id):
    q = get_object_or_404(Questionnaire, pk=quest_id)
    current_answers = request.session.get("current_answers")
    current_p = request.session.get("current_page_id")
    if not current_p or int(current_p) < len(q.page_set.all()):
        if not current_p:
            current_p = 0
        return HttpResponseRedirect(
            reverse('questionnaires.views.go_to_page',
                args=(q.id, int(current_p) + 1,)))
    score = 0
    answer_more = None
    answer_less = None
    results = q.result_set.all()
    for value in current_answers.values():
        score = score + value['score']
    final_result = None
    i = 0
    for i in range(0,len(results)):
        if score < results[i].upper_limit:
            final_result = results[i]
            break
    if final_result:
        if i > 0:
            dw_diff = score - results[i - 1].upper_limit + 1
            answer_less = quest_algorithm.check_result(q, current_answers, dw_diff, True)
        if i < (len(results) - 1):
            up_diff = final_result.upper_limit + 1 - score
            answer_more = quest_algorithm.check_result(q, current_answers, up_diff)
    request.session["current_quest_id"] = None
    request.session["current_page_id"] = None
    request.session["current_answers"] = {}
    return render_to_response('results.html', {
                    'quest': q,
                    'score': score,
                    'result': final_result,
                    'answer_less': answer_less,
                    'answer_more': answer_more
                    }, context_instance=RequestContext(request))


def start(request, quest_id):
    request.session["current_quest_id"] = quest_id
    request.session["current_page_id"] = None
    request.session["current_answers"] = {}
    q = get_object_or_404(Questionnaire, pk=quest_id)
    return render_to_response('start.html', {'quest': q},
                              context_instance=RequestContext(request))


def go_to_page(request, quest_id, page_id):
    q = get_object_or_404(Questionnaire, pk=quest_id)
    page = q.page_set.all()[int(page_id) - 1]
    current_q = request.session.get("current_quest_id")
    current_p = request.session.get("current_page_id")
    if current_q and current_q == quest_id:
        if current_p:
            if int(current_p) > int(page_id):
                return HttpResponseRedirect(
                    reverse('questionnaires.views.go_to_page',
                            args=(current_q, current_p,)))
        else:
            if int(page_id) != 1:
                return HttpResponseRedirect(
                    reverse('questionnaires.views.go_to_page',
                            args=(current_q, '1',)))
    else:
        request.session["current_quest_id"] = quest_id
        request.session["current_answers"] = {}
        pid = page_id
        if int(page_id) != 1:
            pid = 1
        return HttpResponseRedirect(
            reverse('questionnaires.views.go_to_page',
                    args=(q.id, pid,)))
    return render_to_response('page.html', {'quest': q, 'page': page},
                              context_instance=RequestContext(request))


def validate(request, quest_id, page_id):
    q = get_object_or_404(Questionnaire, pk=quest_id)

    page = q.page_set.all()[int(page_id) - 1]
    current_answers = request.session.get("current_answers")
    answers = current_answers
    for question in page.question_set.all():
        try:
            ans = question.answer_set.get(pk=request.POST[str(question.id)])
            answers[question.id] = {'aid': ans.id, 'score': ans.score}
        except (KeyError, Answer.DoesNotExist):
            return render_to_response('page.html', {
                'quest': q, 'page': page,
                'error_message': "You didn't select a choice.",
            }, context_instance=RequestContext(request))

    current_answers = answers
    request.session["current_answers"] = current_answers
    request.session["current_page_id"] = page_id

    if int(page_id) == len(q.page_set.all()):
        return HttpResponseRedirect(
            reverse('questionnaires.views.results',
                    args=(q.id,)))

    return HttpResponseRedirect(
        reverse('questionnaires.views.go_to_page',
                args=(q.id, (int(page_id) + 1))))
