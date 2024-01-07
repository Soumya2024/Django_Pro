from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import *


class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            
            serializer  = FilelistSerializer(data = data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'message' : 'files uploaded Successfully'
                })
            
            return Response({
                'status ' : 400,
                'message' : 'somthing went woring',
                'data' : serializer.errors
            })
            
        except Exception as e:
            print(e)

# Create your views here.


