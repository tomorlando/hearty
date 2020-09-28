from django.shortcuts import render
from django.http import HttpResponse
#from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Information
from . serial import InformationSerializers
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
  return HttpResponse('<h1>Welcome to the heart project!</h1>')

def model(request):
  return HttpResponse('<h1>Page where all details is added + info on heart disease</h1>')

@api_view(['POST'])
def result(request):
  try:
    model = joblib.load('/Users/Tom Orlando/Monash/FIT3164/models/classification/log_reg/log_reg.pkl')
    mydata = request.data
    unit = np.array(list(mydata.values()))
    unit = unit[1:]
    unit = unit.reshape(1, -1)
    scaler = joblib.load('/Users/Tom Orlando/Monash/FIT3164/models/classification/log_reg/scaler.pkl')
    test = scaler.transform(unit)
    ypred = model.predict(test)
    new_df = pd.DataFrame(ypred, columns=['Diagnosis'])
    new_df = new_df.replace({1: 'Likely to have heart disease', 0: 'Not likely to have heart disease'})
    return JsonResponse('{}'.format(new_df), safe=False)
  except ValueError as e:
    return Response(e.args[0], status.HTTP_400_BAD_REQUEST)