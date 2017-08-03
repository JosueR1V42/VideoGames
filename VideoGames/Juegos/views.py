from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import date, datetime
from django.views import generic

# Create your views here.
from .models import *
