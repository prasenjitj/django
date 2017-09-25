# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def home(request):
    num = random.randint(0,1000)
    context = {"html_var": True, "num": num}
    return render(request, "home.html",context)

def about(request):
    num = random.randint(0,1000)
    return render(request, "about.html",{})

def contact(request):
    num = random.randint(0,1000)
    return render(request, "contact.html",{})
