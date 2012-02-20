def check_page(page, answers, lower):
    is_negative = 1
    if lower:
        is_negative = -1
    diff_answer = None
    max_diff = 0
    for question in page.question_set.all():
        new_answer = None
        max_local_diff = 0
        for ans in question.answer_set.all():
            if ans != answers[question.id]:
                diff = ans.score - answers[question.id]['score']
                if (diff * is_negative) > 0:
                    if (diff * is_negative) > max_local_diff:
                        max_local_diff = diff * is_negative
                        new_answer = ans
        if max_local_diff > 0 and max_local_diff > max_diff:
            max_diff = max_local_diff * is_negative
            diff_answer = new_answer
    return {
            'page_id': page.id,
            'answer': diff_answer,
            'difference': max_diff * is_negative
            }


def check_result(quest, answers, difference, lower=False):
    answer = []
    results = []
    for page in quest.page_set.all():
        res = check_page(page, answers, lower)
        if res['answer']:
            results.append(res)
    results.sort(key=lambda x: x['answer'].score, reverse=True)
    for res in results:
        if difference > 0:
            answer.append(res)
            difference = difference - res['difference']
    if difference > 0:
        answer = []
    return answer
