from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Studentdata
from .serializer import StudentSerilzer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def stuu(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seri = StudentSerilzer(data=pythondata)
        if seri.is_valid():
            seri.save()
            res = {'msg': 'Data Created'}
    #json= JSONRenderer().render(seralizer.data)
    
    #return HttpResponse(json, content_type='application/json')
            return JsonResponse(res)
    json_dat= JSONRenderer().render(seri.errors)
    return HttpResponse(json_dat) 
