from django import forms
from django.db import models
import datetime
import pytz

class Guess(models.Model):
    id = models.AutoField(primary_key=True)
    puzzle = models.IntegerField(default=0, null=True)
    studentId = models.IntegerField(default=0, null=True)
    name = models.CharField(max_length=200, null=True)
    guess = models.CharField(max_length=100, null=True)
    correct = models.BooleanField(default=False)
    submitTime = models.DateTimeField(null=True)
    points = models.IntegerField(default=0, null=True)
    
    class Meta:
        db_table = 'Guess'
    def __str__(self):
        output = f'({self.id}) {self.studentId} {self.name}: Puzzle {self.puzzle}: {self.guess}'
        return output

class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    msgTime = models.DateTimeField(null=True)
    msg = models.TextField(max_length=10000, null=True)
    
    class Meta:
        db_table = 'Announcement'
    def __str__(self):
        return f'{self.msgTime.astimezone(pytz.timezone("Australia/Melbourne")).strftime("%d/%m/%Y %I:%M%p").lower()}: {str(self.msg)[:50]} {"..." if len(self.msg) > 50 else ""}'
