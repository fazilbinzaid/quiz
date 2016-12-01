from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from quiz.serializers import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice
from rest_framework.generics import ListCreateAPIView
# from quiz.permissions import IsOwnerOrReadOnly

# Create your views here.

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(APIView):

    def get_object(self, pk):
        try:
            Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response("No such Question")

    def get(self, request, pk, format=None):
        quest = self.get_object(pk)
        choices = Choice.objects.filter(question__id=pk)
        serializer = ChoiceSerializer(choices,context={'request': request} , many=True)
        return Response(serializer.data)

class ChoiceDetail(APIView):

    def get_object(self, request, pk, format=None):
        try:
            Choice.objects.get(pk)
        except Choice.DoesNotExist:
            return Response("No such choice")

    def get(self, request, pk, format=None):
        choices = Choice.objects.get(pk=pk)
        if choices.is_right:
            return Response("You the man!!")
        else:
            return Response("Nop!!")
