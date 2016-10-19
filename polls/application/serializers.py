# -*- coding: utf-8 -*-


def dict_serializer(model, fields):
    return {field: getattr(model, field, None) for field in fields}


class QuestionSerializer(object):
    default_fields = ['id', 'question_text', 'pub_date']

    def __init__(self, question, fields=None):
        self.data = dict_serializer(question, fields or self.default_fields)


class ChoiceSerializer(object):
    default_fields = ['id', 'choice_text', 'votes']

    def __init__(self, question, fields=None):
        self.data = dict_serializer(question, fields or self.default_fields)
