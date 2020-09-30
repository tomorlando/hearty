from django import forms

class PatientForm(forms.Form):
  typical_chest_pain = forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  age=forms.IntegerField()
  dm=forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  ht=forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  fh=forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  tg=forms.IntegerField()
  k=forms.FloatField()
  region_rwma=forms.ChoiceField(choices=[(0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4')])
  bbb=forms.ChoiceField(choices=[(0,'Yes'), (1,'No')])
  tinversion=forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  fbs=forms.IntegerField()
  esr=forms.IntegerField()
  ef_tte=forms.IntegerField()
  dlp=forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  diastolic_murmur=forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])


