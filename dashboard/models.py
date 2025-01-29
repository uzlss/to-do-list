from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True, default=None)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=63)
    tasks = models.ManyToManyField("Task", related_name="tags")

    def __str__(self):
        return self.name
