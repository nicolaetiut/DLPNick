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
                if (diff * is_negative) > 0 and diff > max_local_diff:
                    max_local_diff = diff
                    new_answer = ans
        if max_local_diff > 0 and max_local_diff > max_diff:
            max_diff = max_local_diff
            diff_answer = new_answer
    return {
            'page_id': page.id,
            'answer': diff_answer,
            'difference': max_diff
            }


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
