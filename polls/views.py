# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from polls.application import polls_controller
from polls.application.polls_view import PollsView
from polls.application.serializers import ChoiceSerializer, QuestionSerializer
from polls.framework import get_default_store
from polls.models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    store = get_default_store()
    is_json = request.META.get('HTTP_ACCEPT', None) == 'application/json'
    view = PollsJSONView(request, store) if is_json else PollsHTMLView(request)
    return polls_controller.vote(store, view, question_id, request.POST.get('choice', -1))


class PollsHTMLView(PollsView):

    def __init__(self, request):
        self.request = request

    def log_exception(self, exception):
        raise Http404 from exception

    def ask_question(self, question, error_message=None):
        return render(self.request, 'polls/detail.html', {
            'question': question,
            'error_message': error_message,
        })

    def list_results(self, question):
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class PollsJSONView(PollsView):

    def __init__(self, request, store):
        self.request = request
        self.store = store

    def log_exception(self, exception):
        return JsonResponse({"error": str(exception)}, status=404)

    def ask_question(self, question, error_message=None):
        choices = self.store.questions.get_choices(question)
        data = {
            "question": QuestionSerializer(question).data,
            "choices": [ChoiceSerializer(choice, fields=('id', 'choice_text',)).data for choice in choices]
        }
        status_code = 200
        if error_message:
            data['error_message'] = error_message
            status_code = 400
        return JsonResponse(data, status=status_code)

    def list_results(self, question):
        choices = self.store.questions.get_choices(question)
        return JsonResponse({
            "question": QuestionSerializer(question).data,
            "choices": [ChoiceSerializer(choice).data for choice in choices]
        })
