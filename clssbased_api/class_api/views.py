from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StuSerlaizer
# Create your views here.

class StudentAPI(APIView):
    def get(self, request, pk=None , format=None):
        id= pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serilizer= StuSerlaizer(stu)
            return Response(serilizer.data)
        
    
        stu = Student.objects.all()
        serilizer= StuSerlaizer(stu, many=True)
        return Response(serilizer.data)
    
    def post(self, request, pk=None , format=None):
        serlizer=StuSerlaizer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response({'msg':'Data Created'})
        return Response(serlizer.errors)
    
    def put(self, request, pk=None , format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serlizer = StuSerlaizer(stu, data=request.data )
        serlizer=StuSerlaizer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serlizer.errors)
    
    def patch(self, request, pk=None , format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serlizer = StuSerlaizer(stu, data=request.data , partial=True)
        serlizer=StuSerlaizer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serlizer.errors)
    
    def delete(self, request, pk=None , format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    





       


       
    

