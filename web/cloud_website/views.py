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

# Create your views here.

class InformationView(viewsets.ModelViewSet):
  queryset = Information.objects.all()
  serializer_class = InformationSerializers

def home(request):
  return HttpResponse('<h1>Welcome to the heart project!</h1>')

def output(request):
  return HttpResponse('<h1>The output of model</h1>')

@api_view(['POST'])
def model(request):
  try:
    model = joblib.load('/Users/Tom Orlando/Monash/FIT3164/models/classification/svm/svm_model.pkl')
    #mydata = pd.read_csv('/Users/Tom Orlando/Monash/FIT3164/data/filtered_features/heart_test.csv')
    mydata = request.data
    unit = np.array(list(mydata.values()))
    unit = unit.reshape(1, -1)
    ypred = model.predict(unit)
    ypred = (ypred > 0.5)
    new_df = pd.DataFrame(ypred, columns=['Status'])
    new_df = new_df.replace({True: 'Approved', False: 'Rejected'})
    return JsonResponse('Your status {}'.format(new_df), safe=False)
  except ValueError as e:
    return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 