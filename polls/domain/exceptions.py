# -*- coding: utf-8 -*-


class NotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = kwargs.get('model', None)
        self.filters = kwargs.get('filters', None)

    @property
    def message(self):
        if not self.message:
            model_name = "Unknown model" if not self.model else self.model.__class__.name
            self.message = '%s not found in the store' % (model_name)
            if self.filters:
                self.message = self.message + " with filters: %s" % (str(self.filters),)

    def __str__(self):
        return self.message
