from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
