import datetime
import pytz
import string
from django.conf import settings
import os
tz = pytz.timezone('Australia/Melbourne')

def calcPuzzleState():
    if datetime.datetime.now(tz) > settings.SOLUTION_TIME:
        return 100
    x = (datetime.datetime.now(tz) - settings.INDEX_TIME).days
    if x < 0:
        return 0
    return min(x+1, 4)

def calcSolveTime(puzzleId, guessTime):
    x = guessTime - settings.INDEX_TIME
    return (x.days - puzzleId + 1)*86400 + x.seconds

def calcPuzzleScore(puzzleId, guessTime):
    hours = 9
    if calcSolveTime(puzzleId, guessTime) < hours * 3600:
        return 2
    return 1

def secToHMS(secs):
    secs = int(secs)
    return f'{(secs//3600):02d}:{(secs//60)%60:02d}:{(secs%60):02d}'

def stripGuess(x):
    try:
        x = str(x).upper()
        y = ''.join([i for i in x if i in string.ascii_uppercase])
        return y
    except:
        return ''

def checkGuessCorrect(puzzleId, x):
    answers = {1:('ELIZABETHHOLMES', 'HOLMES'),
               2:('TOXIC'),
               3:('TESTANSWERC'),
               4:('HOMESICKNESS')}
    try:
        z = stripGuess(x) in answers[puzzleId]
        return z
    except:
        return False

def getTitle(puzzleId):
    titles = {1:'Shaping Medicine',
              2:'Wardle',
              3:'Puzzle 3 Title',
              4:'Puzzle 4 TItle'}
    return titles[puzzleId]

def capitaliseAfterSpace(x):
    if len(x) == 0:
        return ''
    x = x.lower()
    y = x[0].upper()
    for i in range(1, len(x)):
        if x[i-1] not in string.ascii_uppercase+string.ascii_lowercase:
            y += x[i].upper()
        else:
            y += x[i]
    return y

def getWardleDictionary():
    with open(os.path.join(settings.BASE_DIR, 'MDSCApp/wardleWords.txt')) as f:
        toRet = [i[:-1].lower() for i in f]
    return toRet

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'