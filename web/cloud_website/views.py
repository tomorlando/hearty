"""
author:Tom
Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response
"""
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Information
from . serial import InformationSerializers
from . forms import PatientForm
import pickle
import json
import numpy
import joblib
import pandas as pd
import numpy as np
# Create your views here.

# The informationView class allows us to query information from the modelsViewSet in which 
# we describe our model of customer (i.e. with all the required features) 
class InformationView(viewsets.ModelViewSet):
  queryset = Information.objects.all()
  serializer_class = InformationSerializers

# Allows us to get data from index.html when the home url is accessed
def home(request):
  return render(request, 'index.html.jinja2')

# Allows us to get data from info.html when the home url is accessed
def information(request):
  return render(request, 'info.html.jinja2')

# Allows us to get data from results_positive.html when the home url is accessed
def results_positive(request):
  return render(request, 'results_positive.html.jinja2')

# Allows us to get data from results_negative.html when the home url is accessed
def results_negative(request):
  return render(request, 'results_negative.html.jinja2')

def cxcontact(request):
  """
  This is the main function which allows us to gather data from the user via the django form
  described in PatientForm() in the forms.py file
  """
  if request.method == 'POST':
    form = PatientForm(request.POST)    # if a form is submitted and valid, we will update following
    if form.is_valid():                 # variables with the input information
        typical_chest_pain = form.cleaned_data['typical_chest_pain']
        age = form.cleaned_data['age']
        dm = form.cleaned_data['dm']
        ht = form.cleaned_data['ht']
        fh = form.cleaned_data['fh']
        tg = form.cleaned_data['tg']
        k = form.cleaned_data['k']
        region_rwma = form.cleaned_data['region_rwma']
        bbb = form.cleaned_data['bbb']
        tinversion = form.cleaned_data['tinversion']
        fbs = form.cleaned_data['fbs']
        esr = form.cleaned_data['esr']
        ef_tte = form.cleaned_data['ef_tte']
        dlp = form.cleaned_data['dlp']
        diastolic_murmur = form.cleaned_data['diastolic_murmur']
        info = (request.POST).dict()      # information from the request.POST will be initialised as a dictionary
        answer = result(info)             # and fed into our result() funtion which queries the model to make a prediciton
        messages.success(request, '{}'.format(answer))      # once a result is sucssessfully returned we post onto the websit
  form = PatientForm()      # If form is not valid, we initalise the form as blank so no error occurs

  return render(request, 'form.html.jinja2', {'form':form})     # wraps our form in the form.html file 

def result(unit):
  """
  This function is where the actual prediction based on a user's input is computed. The input is a dictionary
  with the required features and output is a string describing the model's prediction.
  """
  try:
    model = joblib.load('./cloud_website/models/final_model.pkl')     # first load model from the models file
    mydata = unit     # user input from form as a dictionary
    unit = np.array(list(mydata.values()))    # turn into an array
    unit = unit[1:]       # get rid of the 'intercept' column initialised by numpy
    unit = unit.reshape(1, -1)      # reshape list to be in column vector form
    scaler = joblib.load('./cloud_website/models/scaler.pkl')     # load the scaler used in models
    scaler.clip = False
    test = scaler.transform(unit)       # using the scaler we transform the user input
    ypred = model.predict(test)         # make a prediction using scaled user input and final model
    new_df = pd.DataFrame(ypred, columns=['Diagnosis'])       # add result into a dataframe to make it easier to manipulate
    new_df = new_df.replace({1: 'At risk of heart disease', 0: 'Low risk of heart disease'})    # Change 0 or 1 predictions to string
    return ('{}'.format(new_df.values[0][0]))       # return the values as a string
  except ValueError as e:
    return Response(e.args[0], status.HTTP_400_BAD_REQUEST)       # if bad request from form or bad input raise a 400 BAD REQUEST error


