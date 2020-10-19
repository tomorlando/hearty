"""
author:Tom
Django provides an abstraction layer (the “models”) for structuring and manipulating the data of your Web application
"""
from django.db import models

# Create your models here.

class Information(models.Model):
  CHEST_CHOICE = (
    (1, 'Yes'),
    (0, 'No')
  )
  DM_CHOICE = (
    (1, 'Yes'),
    (0, 'No')
  )
  HT_CHOICE = (
    (1, 'Yes'),
    (0, 'No')
  )
  FH_CHOICE = (
    (1, 'Yes'),
    (0, 'No')
  )
  REGION_CHOICE = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
  )
  BBB_CHOICE = (
    (0, 'Yes'),
    (1, 'No')
  )
  TIN_CHOICE = (
    (1, 'Yes'),
    (0, 'No')
  )
  DLP_CHOICE = (
    (1, 'Yes'),
    (0, 'No')
  )
  MURMUR_CHOICE = (
    (1, 'Yes'),
    (0, 'No')
  )
  typical_chest_pain=models.CharField(max_length=15, choices=CHEST_CHOICE)
  age=models.IntegerField()
  dm=models.CharField(max_length=15, choices=DM_CHOICE)
  ht=models.CharField(max_length=15, choices=HT_CHOICE)
  fh=models.CharField(max_length=15, choices=FH_CHOICE)
  tg=models.IntegerField()
  k=models.FloatField()
  region_rwma=models.CharField(max_length=15, choices=REGION_CHOICE)
  bbb=models.CharField(max_length=15, choices=BBB_CHOICE)
  tinversion=models.CharField(max_length=15, choices=TIN_CHOICE)
  fbs=models.IntegerField()
  esr=models.IntegerField()
  ef_tte=models.IntegerField()
  dlp=models.CharField(max_length=15, choices=DLP_CHOICE)
  diastolic_murmur=models.CharField(max_length=15, choices=MURMUR_CHOICE)

  def __str__(self):
    return self.typical_chest_pain