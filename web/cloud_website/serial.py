
from rest_framework import serializers
from cloud_website.models import Information

class InformationSerializers(serializers.ModelSerializer):
  class Meta:
    model = Information
    fields = '__all__'
