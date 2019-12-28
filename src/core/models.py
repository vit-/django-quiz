import uuid

from django.db import models


def uuid4_str():
    return uuid.uuid4().hex


class Question(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=uuid4_str)
    is_first = models.BooleanField(default=False)  # TODO: only one first question should be allowed
    text = models.CharField(max_length=200)
    next_question = models.ForeignKey('Question', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

    def is_last(self):
        return not bool(self.next_question)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    explanation_text = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
