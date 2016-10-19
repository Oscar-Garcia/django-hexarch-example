# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Entity(ABC):

    @property
    @abstractmethod
    def id(self):
        raise NotImplementedError()


class StoreCollection(ABC):

    @abstractmethod
    def get(self, id) -> Entity:
        raise NotImplementedError()

    def save(self, entity: Entity):
        raise NotImplementedError()


class Store(ABC):

    @property
    @abstractmethod
    def choices(self) -> StoreCollection:
        raise NotImplementedError()

    @property
    @abstractmethod
    def questions(self) -> StoreCollection:
        raise NotImplementedError()
