from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Question, Answer


def question(request, question_pk=None, answer_pk=None):
    if question_pk:
        lookup = {'pk': question_pk}
    else:
        lookup = {'is_first': True}

    try:
        question = Question.objects.prefetch_related('answer_set').get(**lookup)
    except Question.DoesNotExist:
        raise Http404()

    answer = get_object_or_404(Answer, pk=answer_pk) if answer_pk else None

    context = {
        'question': question,
        'answer': answer,
    }
    return render(request, 'question.html', context)
