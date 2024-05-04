from django.db import models

# Create your models here.

class TodoModel(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Date=models.DateField()
    def __str__(self):
        return self.Title
