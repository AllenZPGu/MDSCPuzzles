from django import forms
from .models import *

class GuessForm(forms.Form):
    studentId = forms.IntegerField(required = True, label = "<br>Student ID")
    name = forms.CharField(required = True, max_length = 200, label = "<br>Full name")
    guess = forms.CharField(required = True, max_length = 100, label = "<br>Your guess")