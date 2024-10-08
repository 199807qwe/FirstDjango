from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    text  =  """
    <h1>we  are learnin django</h1>
    <strong>Author<strong>:<i>Ivanov</i>
    """
    return HttpResponse(text)