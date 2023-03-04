from rest_framework import serializers
from .models import Studentdata


class StudentSerilzer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
def create(self, validate_data):
    return Studentdata.objects.create(**validate_data)    
    