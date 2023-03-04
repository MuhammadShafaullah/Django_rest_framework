from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello(request):
#     return Response({'msg':'Hello World'}) 

@api_view(['GET','POST'])
def hello(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg':'Am Get'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Am Post', 'data': request.data})
     
