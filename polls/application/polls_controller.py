# -*- coding: utf-8 -*-
from polls.application.polls_presenter import PollsPresenter
from polls.domain import commands
from polls.domain.exceptions import NotFoundException
from polls.domain.store import Store


def vote(store: Store, presenter: PollsPresenter, question_id, choice_id):
    try:
        question = store.questions.get(question_id)
    except NotFoundException as error:
        return presenter.log_exception(error)
    try:
        commands.vote(store, choice_id)
        return presenter.list_results(question)
    except NotFoundException as error:
        return presenter.ask_question(question, error_message="You didn't select a choice.")
