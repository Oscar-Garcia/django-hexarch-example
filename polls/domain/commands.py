# -*- coding: utf-8 -*-


def vote(store, choice_id):
    choice = store.choices.get(choice_id)
    choice.votes = choice.votes + 1
    store.choices.save(choice)
