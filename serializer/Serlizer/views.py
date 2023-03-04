from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Studentdata
from .serializer import StudentSerilzer
from rest_framework.renderers import JSONRenderer
# Create your views here.


def stuu(request,pk):
    studata=Studentdata.objects.get(id=pk)
    
    seralizer = StudentSerilzer(studata)
    #json= JSONRenderer().render(seralizer.data)
    
    #return HttpResponse(json, content_type='application/json')
    return JsonResponse(seralizer.data)

def stu(request):
    studata=Studentdata.objects.all()
    
    seralizer = StudentSerilzer(studata, many=True)
    #json= JSONRenderer().render(seralizer.data)
    
    #return HttpResponse(json, content_type='application/json')
    return JsonResponse(seralizer.data,safe=False)