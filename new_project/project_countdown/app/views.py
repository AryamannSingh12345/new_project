from django.shortcuts import render
from . import forms
import os
import numpy as np
from . import helper_functions as help
# Create your views here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_countdown.settings')

import django
django.setup()

from app.models import team, answer, score1
team_score = [20, 40, 240]
team_answer = 0
score = 0
numbers_generated = ['', '', '0']
mydata = ''
def home_page(request):
    global team_answer, score
    score = 0
    if request.method == 'POST' and 'team_number' in request.POST:
        team_answer = int(request.POST['Team_number'])
        print(team_answer)
        if team.objects.filter(team_number=team_answer).exists():
            t = team.objects.get(team_number = team_answer)
            t.update_score(0)
            t.save()
            mydata = team.objects.all().order_by('-score').values()
            print(mydata)
        else:
            t = team.objects.get_or_create(team_number = team_answer, score = 0)[0]
            t.save()
    return render(request, 'app/home_page.html', context = {'form' : forms.team_number()})



def index(request):
    global team_answer, score, numbers_generated, mydata
    if request.method == 'POST' and 'number_of_large_numbers' in request.POST:
        team_sol = int(request.POST['enter_the_number_of_large_numbers'])
        numbers_generated = help.number_set_generator(team_sol)

    if request.method == 'POST' and 'user_answer' in request.POST:
        team_sol = request.POST['your_answer']
        print(team_sol)
        print(numbers_generated[0])
        try:
            points = help.is_correct(team_sol, numbers_generated[0], int(numbers_generated[2]))
            score += points
        except:
            pass
        t = team.objects.get(team_number = team_answer)
        t.update_score(score)
        t.save()
        numbers_generated[0] = ''
        numbers_generated[2] = '0'
        mydata = team.objects.all().order_by('-score').values()
        print(mydata)

    return render(request, 'app/index.html', context = {'score' : score, 'numbers' : numbers_generated[0], 'target' : numbers_generated[2], 'form1':forms.large_numbers(), 'form' : forms.answer()})

def end(request):
    global mydata
    list = []
    for data in mydata:
        list.append(data['team_number'])
    '''team.objects.all().delete()'''
    return render(request, 'app/end.html', context = {'winners' : list})
