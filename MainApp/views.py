from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    text  =  """
    <h1>we  are learnin django</h1>
    <strong>Author<strong>:<i>Ivanov</i>
    """
    return HttpResponse(text)

def about(request):
    text  =  """
    <h2>Имя: Иван</h2>
    <h2>Отчество: Петрович</h2>
    <h2>Фамилия: Иванов</h2>
    <h2>телефон: 8-923-600-01-02</h2>
    <h2>email: vasya@mail.ru</h2>
    <strong>Author<strong>:<i>Ivanov</i>
    """
    return HttpResponse(text)