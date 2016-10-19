# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class PollsView(ABC):

    @abstractmethod
    def log_exception(self, exception):
        raise NotImplementedError()

    @abstractmethod
    def ask_question(self, question, error_message=None):
        raise NotImplementedError()

    @abstractmethod
    def list_results(self, question):
        raise NotImplementedError()
