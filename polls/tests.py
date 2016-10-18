# -*- coding: utf-8 -*-
import datetime
import random

import pytest
from django.core.urlresolvers import reverse
from django.utils import timezone
from django_seed import Seed

from polls.models import Question, Choice


@pytest.fixture
def seed():
    return Seed.seeder()


def test_was_published_recently_with_future_question():
    """
    was_published_recently() should return False for questions whose
    pub_date is in the future.
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    assert not future_question.was_published_recently()


@pytest.mark.django_db(transaction=False)
def test_max_polls(client, seed):
    """
    Test that the maximun number of polls returned on the index view
    """

    seed.add_entity(Question, 10)
    seed.execute()

    response = client.get(reverse('polls:index'))
    response.status_code = 200
    assert len(response.context['latest_question_list']) == 5


@pytest.mark.django_db(transaction=False)
def test_vote(client, seed):
    """
    Test that the vote is counted.
    """
    seed.add_entity(Choice, 3, {'votes': 0})
    data = seed.execute()
    choice_id = random.choice(data[Choice])
    choice = Choice.objects.get(pk=choice_id)
    assert choice.votes == 0
    question_id = choice.question.id

    client.post(reverse('polls:vote', args=(question_id,)), {'choice': choice_id})

    choice.refresh_from_db()
    assert choice.votes == 1
