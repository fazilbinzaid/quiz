from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    owner = models.ForeignKey('auth.User', related_name='questions')
    question_text = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='of_question')
    choice_text = models.CharField(max_length=50)
    is_right = models.BooleanField()

    def __str__(self):
        return self.choice_text
