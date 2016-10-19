# -*- coding: utf-8 -*-


class NotFoundException(Exception):
    def __init__(self, *args, message=None, model=None, filters=None):
        super().__init__(*args)
        self.model = model
        self.filters = filters
        self._message = message

    @property
    def message(self):
        if not self._message:
            model_name = "Unknown model" if not self.model else self.model.__name__
            self._message = '%s not found in the store' % (model_name)
            if self.filters:
                self._message = self._message + " with filters: %s" % (str(self.filters),)
        return self._message

    def __str__(self):
        return self.message
