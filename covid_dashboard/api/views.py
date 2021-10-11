from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .util import Reverse_String



# Create your views here.

class SampleEndpoint(APIView):

    def post(self, request, format=None):

        input_payload = self.request.data
        output_payload = None 

        output_payload=Reverse_String(input_payload)

        return Response(output_payload,status=status.HTTP_200_OK);
