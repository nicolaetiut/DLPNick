def check_page(page, answers, lower):
    is_negative = 1
    if lower:
        is_negative = -1
    diff_answer = None
    max_difference = 0
    for question in page.question_set.all():
        new_answer = None
        max_local_difference = 0
        for answer in [a for a in question.answer_set.all() if a != answers[question.id]['score']]:
            diff = answer.score - answers[question.id]['score']
            if (diff * is_negative) > 0 and diff > max_local_difference:
                max_local_difference = diff
                new_answer = answer
        if max_local_difference > 0 and max_local_difference > max_difference:
            max_difference = max_local_difference
            diff_answer = new_answer
    return {'page_id':page.id, 'answer': diff_answer, 'difference': max_difference}


def check_result(quest, answers, difference, lower=False):
    answer = []
    results = []
    for page in quest.page_set.all():
        results.append(check_page(page, answers, lower))
    results.sort(key=lambda x: x['answer'].score, reverse=True)
    for res in results:
        if difference > 0:
            answer.append(res)
            difference = difference - res['difference']
    if difference > 0:
        answer = []

    return answer
            