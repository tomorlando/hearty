from django.db import models

# Create your models here.

class Information(models.Model):
  CHEST_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )
  DM_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )
  HT_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )
  FH_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )
  REGION_CHOICE = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
  )
  BBB_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )
  TIN_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )
  DLP_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )
  MURMUR_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No')
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