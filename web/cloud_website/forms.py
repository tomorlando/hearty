"""

Author:Tom


Django provides a rich framework to facilitate the creation of forms and the manipulation of form data.
"""
from django import forms

class PatientForm(forms.Form):
  typical_chest_pain = forms.ChoiceField(choices = [(0,'No'), (1,'Yes')])
  age = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Enter patient age'}))
  dm = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  ht = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  fh = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  tg = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Enter patient TG'}), help_text='120-150 if unsure')
  k = forms.FloatField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Enter patient K'}), help_text='4.2-4.23 if unsure')
  region_rwma = forms.ChoiceField(choices=[(0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4')])
  bbb = forms.ChoiceField(choices=[(1,'No'), (0,'Yes')])
  tinversion = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  fbs = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Enter patient FBS'}), help_text='98-120 if unsure')
  esr = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Enter patient ESR'}), help_text='15-19 if unsure')
  ef_tte = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Enter patient EF-TTE'}), help_text='47-50 if unsure')
  dlp = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  diastolic_murmur = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])


