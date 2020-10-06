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

class InformationView(viewsets.ModelViewSet):
  queryset = Information.objects.all()
  serializer_class = InformationSerializers

def home(request):
  return render(request, 'index.html')

def information(request):
  return render(request, 'info.html')

def result(unit):
  try:
    model = joblib.load('/Users/Tom Orlando/Monash/FIT3164/models/classification/log_reg/log_reg.pkl')
    mydata = unit
    unit = np.array(list(mydata.values()))
    unit = unit[1:]
    unit = unit.reshape(1, -1)
    scaler = joblib.load('/Users/Tom Orlando/Monash/FIT3164/models/classification/log_reg/scaler.pkl')
    test = scaler.transform(unit)
    ypred = model.predict(test)
    new_df = pd.DataFrame(ypred, columns=['Diagnosis'])
    new_df = new_df.replace({1: 'At risk of heart disease', 0: 'No risk of heart disease'})
    return ('{}'.format(new_df.values[0][0]))
  except ValueError as e:
    return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def cxcontact(request):
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
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
        info = (request.POST).dict()
        answer = result(info)
        messages.success(request, '{}'.format(answer))      
  form = PatientForm()

  return render(request, 'form/cxform.html', {'form':form})


