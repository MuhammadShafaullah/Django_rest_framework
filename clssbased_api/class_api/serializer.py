from rest_framework import serializers
from .models import Student
from rest_framework import serializers

#1st Basic example

#Using Model Serilazer
class StuSerlaizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']



        
# By using Model Serilaizer we can get create and update auto not need to write      
        
# 2nd example when we need to determine properties of field

# class StuSerlaizer(serializers.ModelSerializer):
#     #name = serializers.CharField(read_only=True)
#     class Meta:
#         model = Student
#         fields = ['name', 'roll', 'city']
#         read_only_fields = ['name','roll']
#         # Filed level validation
#         def validate_roll(self, value):
#             if value >=200:
#                 raise serializers.ValidationError('Out of memory')
#             return value

#// how to add two number in python?
 
  