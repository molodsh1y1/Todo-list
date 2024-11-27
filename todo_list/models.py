from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True
    )

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self) -> str:
        return self.content
