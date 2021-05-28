from django.db import models


class ToDoItem(models.Model):
    work = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.work
