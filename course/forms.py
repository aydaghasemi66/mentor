from django import forms
from .models import Comment, Reply


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['which_course', 'user', 'email', 'subject', 'message']


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['which_comment', 'user', 'message']