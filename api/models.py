from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __repr__(self):
        return self.title