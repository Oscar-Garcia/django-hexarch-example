# -*- coding: utf-8 -*-
from polls.application.polls_view import PollsView
from polls.domain import commands
from polls.domain.exceptions import NotFoundException
from polls.domain.store import Store


def vote(store: Store, view: PollsView, question_id, choice_id):
    try:
        question = store.questions.get(question_id)
    except NotFoundException as error:
        return view.log_exception(error)
    try:
        commands.vote(store, choice_id)
        return view.list_results(question)
    except NotFoundException as error:
        return view.ask_question(question, error_message="You didn't select a choice.")
