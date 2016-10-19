# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from polls.application import polls_controller
from polls.application.polls_view import PollsView
from polls.framework.django_store import DjangoStore
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
    presenter = PollsHTMLView(request)
    store = DjangoStore()
    return polls_controller.vote(store, presenter, question_id, request.POST.get('choice', -1))


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
