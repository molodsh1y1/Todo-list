import datetime
from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import TaskForm, TagForm

from .models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.prefetch_related(
        "tags"
    ).order_by(
        "is_done",
        "-created_at"
    )

    return render(
        request,
        "todo_list/index.html",
        {
            "task_list": tasks,
            "datetime_now": datetime.now()
        }
    )


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo:index")


class TagUpdateView(generic.UpdateView):
    form_class = TagForm
    model = Tag
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
