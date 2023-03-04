from rest_framework import serializers
from .models import Studentdata


class StudentSerilzer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    