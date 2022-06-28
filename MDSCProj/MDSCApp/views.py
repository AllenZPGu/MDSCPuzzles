import json
from django import forms
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max
from django.forms import formset_factory, ValidationError
from django.http import JsonResponse, FileResponse, Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
# from datetime import datetime

from .forms import *
from .models import *
import os
import string
from .utils import *
import random
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

    puzInfo = {'puzId':puzzleId, 'title':getTitle(puzzleId)}
    specificArgs = {}
    if puzzleId == 1:
        specificArgs['pplRange'] = range(1,18)

    return render(request, f'MDSCApp/puzzlePages/puzzle{puzzleId}.html', {'puzInfo':puzInfo, 'specificArgs':specificArgs})

def puzzlePDF(request, puzzleId):
    try:
        if puzzleId > calcPuzzleState() or puzzleId not in (1,3,4):
            raise Http404()
    except:
        raise Http404()

    try:
        return FileResponse(open(os.path.join(settings.BASE_DIR, f'MDSCApp/pdf/Puzzle{puzzleId}.pdf'), 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("PDF file not found!")

def puzzles(request):
    puzInfo = []
    for puz in range(1,5):
        x = Guess.objects.filter(puzzle=puz)
        puzInfo.append({'id': puz, 'title': getTitle(puz), 'solves': len(x.filter(correct=True)), 'guesses': len(x)})
    return render(request, 'MDSCApp/puzzles.html', {'puzzleState':calcPuzzleState(), 'puzInfo':puzInfo})

def solve(request, puzzleId):
    try:
        if puzzleId > calcPuzzleState() or puzzleId < 1 or puzzleId > 4:
            raise Http404()
    except:
        raise Http404()

    puzInfo = {'puzId':puzzleId, 'title':getTitle(puzzleId)}

    if request.method == 'POST':
        guessForm = GuessForm(request.POST)
        if guessForm.is_valid():
            if Guess.objects.filter(studentId=guessForm.cleaned_data.get('studentId'), puzzle=puzzleId, correct=True):
                guessForm = GuessForm()
                return render(request, f'MDSCApp/puzzlePages/solve.html', {'guessForm':guessForm, 'state':'duplicate', 'puzInfo':puzInfo})
            newGuess = Guess()
            newGuess.puzzle = puzzleId
            newGuess.studentId = guessForm.cleaned_data.get('studentId')
            newGuess.name = guessForm.cleaned_data.get('name')
            newGuess.guess = stripGuess(guessForm.cleaned_data.get('guess'))
            newGuess.correct = checkGuessCorrect(puzzleId, newGuess.guess)
            newGuess.submitTime = datetime.datetime.now(tz)
            if newGuess.correct:
                newGuess.points = calcPuzzleScore(puzzleId, newGuess.submitTime)
            newGuess.save()

            if newGuess.correct:
                return render(request, f'MDSCApp/puzzlePages/solved.html', {'puzInfo':puzInfo, 'guess':newGuess.guess, 'points':newGuess.points*500})
            else:
                guessForm = GuessForm(initial={'studentId':newGuess.studentId, 'name':newGuess.name})
                return render(request, f'MDSCApp/puzzlePages/solve.html', {'guessForm':guessForm, 'state':'wrong', 'guess':newGuess.guess, 'puzInfo':puzInfo})
    else:
        guessForm = GuessForm()
    
    return render(request, f'MDSCApp/puzzlePages/solve.html', {'guessForm':guessForm, 'state':'new', 'puzInfo':puzInfo})

def leaderboard(request):
    allGuesses = Guess.objects.exclude(points=0)
    ids = list(set([i.studentId for i in allGuesses]))
    dictList = []
    for stuId in ids:
        stuGuesses = allGuesses.filter(studentId=stuId)
        x = {'studentId':stuId,
             'name':capitaliseAfterSpace(stuGuesses[0].name),
             'outcomes': [(0,'') for i in range(4)],
             'points': 0,
             'puzzs': 0,
             'avgSolveTime': -1,
             'totSolveTime': 0}
        for stuGuess in stuGuesses:
            x['outcomes'][stuGuess.puzzle-1] = (stuGuess.points, secToHMS(calcSolveTime(stuGuess.puzzle, stuGuess.submitTime)))
            x['puzzs'] += 1
            x['totSolveTime'] += calcSolveTime(stuGuess.puzzle, stuGuess.submitTime)
        try:
            x['avgSolveTime'] = secToHMS(x['totSolveTime'] // x['puzzs'])
        except:
            pass
        x['points'] = 500 * sum(x['outcomes'][i][0] for i in range(4))
        dictList.append(x)
    dictList = sorted(dictList, key=lambda y: 1000000 * y['points'] + 1000000 *y['puzzs'] - y['totSolveTime'])
    dictList.reverse()
    return render(request, f'MDSCApp/leaderboard.html', {'dictList':dictList})

def wardle(request, wardleId):
    try:
        if calcPuzzleState() <= 0 or wardleId not in ("1","2","3","4","5","infinity"):
            raise Http404()
    except:
        raise Http404()
    return render(request, 'MDSCApp/puzzlePages/wardle.html', {'wardleId':wardleId})


def wardleAjax(request):
    targetList = ['heart', 'atopy', 'shiga', 'lasix', 'lumen', 'toxic']
    if not is_ajax(request):
        raise Http404()
    if request.method == "GET":
        wardleId = request.GET.get("wardleId")
        tempId = int(wardleId) if wardleId != 'infinity' else 6
        if tempId != 6:
            return JsonResponse({"dictionary":getWardleDictionary(), "targetWord":targetList[tempId-1]}, status = 200)
        else:
            return JsonResponse({"dictionary":targetList, "targetWord":targetList[tempId-1]}, status = 200)
    else:
        return JsonResponse({}, status=400)

def announcements(request):
    x = list(Announcement.objects.all())
    x = sorted(x, key=lambda z:z.msgTime)
    y = []
    for i in x:
        a = i.msgTime.astimezone(tz)
        if a > datetime.datetime.now(tz):
            continue
        y.append({'msgTime': f'{a.strftime("%a")} {a.strftime("%d/%m/%Y %I:%M%p").lower()}',
        'msg': i.msg})
    y.reverse()
    return render(request, 'MDSCApp/announcements.html', {'announcements':y})

def wardleCasual(request):
    return render(request, 'MDSCApp/puzzlePages/wardleCasual.html')


def wardleAjaxCasual(request):
    if not is_ajax(request):
        raise Http404()
    if request.method == "GET":
        x = getWardleDictionary()
        return JsonResponse({"dictionary":x, "targetWord":random.choice(x)}, status = 200)
    else:
        return JsonResponse({}, status=400)