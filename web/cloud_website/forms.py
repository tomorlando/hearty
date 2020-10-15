from django import forms

class PatientForm(forms.Form):
  typical_chest_pain = forms.ChoiceField(choices = [(0,'No'), (1,'Yes')])
  age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient age'}))
  dm = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  ht = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  fh = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  tg = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient TG'}), help_text='120-150.3 if unsure')
  k = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient K'}), help_text='4.2-4.23 if unsure')
  region_rwma = forms.ChoiceField(choices=[(0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4')])
  bbb = forms.ChoiceField(choices=[(1,'No'), (0,'Yes')])
  tinversion = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  fbs = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient FBS'}), help_text='98-119.2 if unsure')
  esr = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient ESR'}), help_text='15-19.46 if unsure')
  ef_tte = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient EF-TTE'}), help_text='47.2-50 if unsure')
  dlp = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])
  diastolic_murmur = forms.ChoiceField(choices=[(0,'No'), (1,'Yes')])


