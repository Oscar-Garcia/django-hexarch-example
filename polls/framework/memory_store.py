# -*- coding: utf-8 -*-
import factory
from faker import Factory as FakerFactory

from polls.domain.exceptions import NotFoundException
from polls.domain.store import Store, StoreCollection

faker = FakerFactory.create()


class Choice(object):
    def __init__(self, id=None, question=None, choice_text=None, votes=0):
        self.id = id
        self.question = question
        self.choice_text = choice_text
        self.votes = votes


class Question(object):
    def __init__(self, id=None, question_text=None, pub_date=None):
        self.id = id
        self.question_text = question_text
        self.pub_date = pub_date


class MemoryAdapter(StoreCollection):
    def __init__(self, model_class):
        self._model_class = model_class
        self._cache = {}

    def all(self):
        return self._cache.values()

    def get(self, id):
        try:
            return self._cache[int(id)]
        except KeyError as error:
            raise NotFoundException(model=self._model_class, filters={'id': id}) from error

    def save(self, entity):
        if not entity.id:
            entity.id = len(self._cache) + 1
        self._cache[entity.id] = entity

    def save_batch(self, entities):
        for entity in entities:
            self.save(entity)


class QuestionMemoryAdapter(MemoryAdapter):

    def __init__(self, model_class, store):
        self.store = store
        super().__init__(model_class)

    def get_choices(self, question):
        return [choice for choice in self.store.choices.all() if choice.question.id == question.id]


class MemoryStore(Store):

    def __init__(self):
        self._choices = MemoryAdapter(Choice)
        self._questions = QuestionMemoryAdapter(Question, self)

    @property
    def choices(self):
        return self._choices

    @property
    def questions(self):
        return self._questions


class FakeQuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    pub_date = factory.LazyAttribute(lambda x: faker.date_time_this_month(before_now=True, after_now=False))


class FakeChoiceFactory(factory.Factory):
    class Meta:
        model = Choice

    question = factory.SubFactory(FakeQuestionFactory)
    choice_text = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    votes = 0
