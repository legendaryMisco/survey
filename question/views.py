from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse, get_object_or_404, redirect
from .models import *

def index(request):
    questions = Question.objects.all()[0]
    context = {'questions':questions}

    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            # return HttpResponseRedirect(reverse('index'))
            return render(request, 'question/survey.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('second')
    return render(request, 'question/survey.html', context)


def secondQuestion(request):
    questions = Question.objects.all()[0]
    context = {'questions':questions}
    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            return render(request, 'question/questions.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('third')
    return render(request, 'question/questions.html', context)


def thirdQuestion(request):
    questions = Question.objects.all()[1]
    context = {'questions':questions}
    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            return render(request, 'question/questions.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('fourth')
    return render(request, 'question/questions.html', context)


def fourthQuestion(request):
    questions = Question.objects.all()[2]
    context = {'questions':questions}
    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            return render(request, 'question/questions.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('fifth')
    return render(request, 'question/questions.html', context)


def fifthQuestion(request):
    questions = Question.objects.all()[3]
    context = {'questions':questions}
    if request.method == 'POST':
        try:
            selected_choice = questions.choice_set.get(pk=request.POST['question'])
        except:
            return render(request, 'question/questions.html', {"error_message":"You did not choose an option"})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('sixth')
    return render(request, 'question/questions.html', context)


def sixthuestion(request):
    questions = Question.objects.all()[4]

    if request.method == 'POST':
        Choice.objects.create(
            question = questions,
            choice_text = request.POST['choice']
        )
        return HttpResponse('Thank you for yur Time')

    context = {'questions': questions}
    return render(request, 'question/answer.html',context)


def Votes(request):
    questions = Question.objects.all()

    context = {'question': questions}
    return render(request, 'question/account.html',context)











