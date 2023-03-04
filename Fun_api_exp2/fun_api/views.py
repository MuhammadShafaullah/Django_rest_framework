from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StuSerlaizer
# Create your views here.

@api_view(['GET','POST','PUT','PACH','DELETE'])
def hello(request):
    if request.method == 'GET':
        id= request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serilizer= StuSerlaizer(stu)
            return Response(serilizer.data)
        
    
        stu = Student.objects.all()
        serilizer= StuSerlaizer(stu, many=True)
        return Response(serilizer.data)

    if request.method == 'POST':
        serlizer=StuSerlaizer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response({'msg':'Data Created'})
        return Response(serlizer.errors)
    

    if request.method == 'PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serlizer = StuSerlaizer(stu, data=request.data , partial=True)
        serlizer=StuSerlaizer(data=request.data)
        if serlizer.is_valid():
            serlizer.save()
            return Response({'msg':'Data Updated'})
        return Response(serlizer.errors)
   
    if request.method == 'DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    return Response(serlizer.errors)
          
