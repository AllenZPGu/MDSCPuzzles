import json
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max
from django.forms import formset_factory, ValidationError
from django.http import JsonResponse, FileResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.views.decorators.cache import never_cache
from django.views.decorators.http import last_modified
from django.contrib.auth.models import User
# from datetime import datetime

from .forms import *
from .models import *
import os
import string
from .utils import *
# import requests
# import csv
# from io import StringIO
import datetime
import pytz
tz = pytz.timezone('Australia/Melbourne')


# Create your views here.
def index(request):
    return render(request, 'MDSCApp/index.html', {'DEVMODE':settings.DEVMODE, 'DEBUG':settings.DEBUG})

def instructions(request):
    return render(request, 'MDSCApp/instructions.html')

def puzzle(request, puzzleId):
    try:
        if puzzleId > calcPuzzleState() or puzzleId < 1 or puzzleId > 4:
            raise Http404()
    except:
        raise Http404()
    return render(request, f'MDSCApp/puzzlePages/puzzle{puzzleId}.html')

def puzzles(request):
    return render(request, 'MDSCApp/puzzles.html', {'puzzleState':calcPuzzleState()})

def solve(request, puzzleId):
    try:
        if puzzleId > calcPuzzleState() or puzzleId < 1 or puzzleId > 4:
            raise Http404()
    except:
        raise Http404()

    if request.method == 'POST':
        guessForm = GuessForm(request.POST)
        if guessForm.is_valid():
            if Guess.objects.filter(studentId=guessForm.cleaned_data.get('studentId')).filter(correct=True):
                guessForm = GuessForm()
                return render(request, f'MDSCApp/puzzlePages/solve{puzzleId}.html', {'guessForm':guessForm, 'state':'duplicate'})
            newGuess = Guess()
            newGuess.puzzle = puzzleId
            newGuess.studentId = guessForm.cleaned_data.get('studentId')
            newGuess.name = guessForm.cleaned_data.get('name')
            newGuess.guess = stripGuess(guessForm.cleaned_data.get('guess'))
            newGuess.correct = checkGuessCorrect(puzzleId, guessForm.cleaned_data.get('guess'))
            newGuess.submitTime = datetime.datetime.now(tz)
            if newGuess.correct:
                newGuess.points = calcPuzzleScore(puzzleId, newGuess.submitTime)
            newGuess.save()

            if newGuess.correct:
                return render(request, f'MDSCApp/puzzlePages/solved.html', {'puzzleId':puzzleId, 'title':getTitles(puzzleId), 'guess':newGuess.guess, 'points':newGuess.points})
            else:
                guessForm = GuessForm(initial={'studentId':newGuess.studentId, 'name':newGuess.name})
                return render(request, f'MDSCApp/puzzlePages/solve{puzzleId}.html', {'guessForm':guessForm, 'state':'wrong', 'guess':newGuess.guess})
    else:
        guessForm = GuessForm()
        return render(request, f'MDSCApp/puzzlePages/solve{puzzleId}.html', {'guessForm':guessForm, 'state':'new'})

def leaderboard(request):
    allGuesses = Guess.objects.exclude(points=0)
    ids = list(set([i.studentId for i in allGuesses]))
    dictList = []
    for stuId in ids:
        stuGuesses = allGuesses.filter(studentId=stuId)
        x = {'studentId':stuId,
             'name':stuGuesses[0].name,
             'outcomes': [(0,'') for i in range(4)],
             'points': 0}
        for stuGuess in stuGuesses:
            x['outcomes'][stuGuess.puzzle] = (stuGuess.points, secToHMS(calcSolveTime(stuGuess.puzzle, stuGuess.submitTime)))
        x['points'] = 500 * sum(x['outcomes'][i][0] for i in range(4))
        dictList.append(x)
    dictList = sorted(dictList, key=lambda y:-y['points']-sum([i[0]>0 for i in y['outcomes']]))
    return render(request, f'MDSCApp/leaderboard.html', {'dictList':dictList})