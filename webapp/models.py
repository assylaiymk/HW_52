from django.db import models


class Task(models.Model):
    name = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Text', max_length=3000, null=False, blank=False)
    due_date = models.DateTimeField(verbose_name='Due date', max_length=300)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.description} - {self.due_date}'
