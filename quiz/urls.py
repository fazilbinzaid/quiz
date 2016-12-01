from django.conf.urls import include, url
from .models import Question, Choice
from quiz.views import QuestionList, QuestionDetail, ChoiceDetail


urlpatterns = [
    url(r'^question/$', QuestionList.as_view(), name='question-list'),
    url(r'^question/(?P<pk>[0-9]+)/$', QuestionDetail.as_view(), name='quizzy'),
    url(r'^choice-(?P<pk>[0-9]+)/$', ChoiceDetail.as_view(), name='choice-detail'),

]
