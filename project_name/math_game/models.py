from django.db import models

# Create your models here.
class MathQuestion(models.Model):
    LEVEL_CHOICES = [
        ('1', 'Addition'),
        ('2', 'Subtraction'),
        ('3', 'Division'),
        ('4', 'Multiplication'),
    ]

    question = models.CharField(max_length=255)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    correct_answer = models.IntegerField()

    def __str__(self):
        return self.question