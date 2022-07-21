from django import forms

from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'number', 'made']
        labels = {
            'subject': '제품명',
            'number': '가격',
            'made': '제조사',

        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
