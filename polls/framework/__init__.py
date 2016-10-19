# -*- coding: utf-8 -*-
from .django_store import DjangoStore

DEFAULT_STORE = None

def get_default_store():
    return DEFAULT_STORE or DjangoStore()


class DefaultStore:
    def __init__(self, store):
        self._new_store = store
        self._old_store = DEFAULT_STORE

    def __enter__(self):
        global DEFAULT_STORE
        DEFAULT_STORE = self._new_store
        return self._new_store

    def __exit__(self, type, value, traceback):
        global DEFAULT_STORE
        DEFAULT_STORE = self._old_store
