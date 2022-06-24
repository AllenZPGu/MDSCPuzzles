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
# from datetime import datetime

# from .forms import *
from .models import *
import os
# from .utils import *
# import requests
# import csv
# from io import StringIO
import datetime

# Create your views here.
def index(request):
    return render(request, 'MDSCApp/index.html')

def instructions(request):
    return render(request, 'MDSCApp/instructions.html')

def puzzles(request):
    return render(request, 'MDSCApp/puzzles.html', {'puzzleState':3})
