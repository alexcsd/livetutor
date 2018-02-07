from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Question, Answer, Reply
# Create your views here.
def index(request):
    return render(request, 'blogask/index.html')

def questions_view(request):
    questions = Question.objects.all()
    return render(request, 'blogask/questions.html',{'questions':questions})

def create_question(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            question = Question()
            question.content = request.POST['content']
            question.user = request.user
            question.save()
            return redirect('questions')
        else:
            return render(request, 'blogask/createquestion.html')
    return redirect('questions')
def question_view(request, pk):
    question = Question.objects.get(pk = pk)
    answers = Answer.objects.filter(question=question)
    replys = Reply.objects.filter(question=question)
    context = {
        'question':question,
        'answers':answers,
        'replys':replys
    }
    return render(request, 'blogask/question.html', context)

def answer(request, pk):
    if request.user.is_authenticated:
        if request.method=="POST":
            question = Question.objects.get(pk = pk)
            answer = Answer()
            answer.content = request.POST['answer']
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('question',pk)
        else:
            return redirect('question',pk,{'error_msg':'wrong url'})
    return redirect('question',pk)

def reply(request, pk):
    if request.user.is_authenticated:
        if request.method=="POST":
            answer = Answer.objects.get(pk = pk)
            question = answer.question
            reply = Reply()
            reply.content = request.POST['reply']
            reply.question = question
            reply.answer = answer
            reply.user = request.user
            reply.save()
            return redirect('question',question.pk)
        else:
            return redirect('question',question.pk,{'error_msg':'wrong url'})
    return redirect('question',question.pk)

def register_user(request):
    form = UserCreationForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'blogask/register.html',{'form':form,'error_message':'wrong auth'})

    return render(request, 'blogask/register.html',{'form':form})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'blogask/login.html', {'error_message':'wrong auth'})

    return render(request, 'blogask/login.html')
def logout_user(request):
    logout(request)
    return redirect('index')