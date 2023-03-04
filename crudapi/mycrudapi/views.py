from django.shortcuts import render,HttpResponse
import io 
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StutSerilaizer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method == 'GET' :
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            slizer = StutSerilaizer(stu)
            json_data = JSONRenderer().render(slizer.data)
            return HttpResponse(json_data, content_type='appliction/josn')
        
        stu = Student.objects.all()
        slizerr = StutSerilaizer(stu, many=True)
        json_data = JSONRenderer().render(slizerr.data)
        return HttpResponse(json_data, content_type='appliction/josn')
        
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StutSerilaizer(data= pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        slizerr = StutSerilaizer(stu, data= pythondata, partial=True)
        
        if slizerr.is_valid():
            slizerr.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(slizerr.errors)
        return HttpResponse(json_data, content_type='application/json')
     
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id =pythondata.get('id')
        stu =Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted!!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(slizerr.errors)
    return HttpResponse(json_data, content_type='application/json')
            
        
        