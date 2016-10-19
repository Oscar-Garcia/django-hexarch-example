# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from polls.models import Choice, Question
from polls.domain.store import Store, StoreCollection
from polls.domain.exceptions import NotFoundException


class ModelAdapter(StoreCollection):
    def __init__(self, model_class):
        self._model_class = model_class

    def get(self, id):
        try:
            return self._model_class.objects.get(pk=id)
        except ObjectDoesNotExist as error:
            raise NotFoundException(model=self._model_class, filters={'id': id}) from error

    def save(self, entity):
        entity.save()


class DjangoStore(Store):

    @property
    def choices(self):
        return ModelAdapter(Choice)

    @property
    def questions(self):
        return ModelAdapter(Question)
