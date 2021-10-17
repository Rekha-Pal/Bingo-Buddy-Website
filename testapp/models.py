from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    A = models.CharField(max_length=200)
    B = models.CharField(max_length=200)
    C = models.CharField(max_length=200)
    D = models.CharField(max_length=200)
    answer = models.CharField(max_length=10)

    def __str__(self):
        return self.question

