from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Task")
    content = models.TextField()
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
