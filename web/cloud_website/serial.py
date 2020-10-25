"""
Author: Tom Orlando
This file is built to link the form and models sections of the django backend.
"""


from rest_framework import serializers
from cloud_website.models import Information

class InformationSerializers(serializers.ModelSerializer):
  """
  This class leverages the existing serializers provided by the django framework
  """
  class Meta:
    model = Information
    fields = '__all__'
