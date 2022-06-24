from django import forms
from django.db import models

class Guess(models.Model):
    id = models.AutoField(primary_key=True)
    puzzle = models.IntegerField(default=0, null=True)
    studentId = models.IntegerField(default=0, null=True)
    name = models.CharField(max_length=200, null=True)
    guess = models.CharField(max_length=100, null=True)
    correct = models.BooleanField(default=False)
    submitTime = models.DateTimeField(null=True)
    
    class Meta:
        db_table = 'Guess'
    def __str__(self):
        output = f'{self.id}'
        return output