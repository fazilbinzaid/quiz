from .models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    # question_text = serializers.CharField(max_length=50)
    owner = serializers.ReadOnlyField(source='owner.username')
    of_question = serializers.HyperlinkedIdentityField(view_name='quizzy',)

    class Meta:
        model = Question
        fields = ('of_question', 'id', 'question_text', 'owner')

class ChoiceSerializer(serializers.ModelSerializer):
    is_right = serializers.HiddenField(default='is_right')
    url = serializers.HyperlinkedIdentityField(view_name='choice-detail')

    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'is_right', 'url')

# class UserSerializer(serializers.ModelSerializer):
# #
#     class Meta:
