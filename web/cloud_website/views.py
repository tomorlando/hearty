from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('<h1>Welcome to the Heart Disease detection tool!</h1>')

def model(request):
  return HttpResponse('<h1>Heart check page</h1>')

def output(request):
  return HttpResponse('<h1>The output of model</h1>')