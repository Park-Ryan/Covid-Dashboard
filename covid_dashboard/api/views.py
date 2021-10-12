from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from covid_dashboard.api.data_layer.load_csv import Country
from .util import Reverse_String
from .serializers import *
from .data_layer import load_csv
import json
# Create your views here.

class SampleEndpoint(APIView):

    def post(self, request, format=None):

        input_payload = self.request.data
        output_payload = None 

        output_payload=Reverse_String(input_payload)

        return Response(output_payload,status=status.HTTP_200_OK)

    def encoder_country(country):

        if(isinstance(country, load_csv.Country)):
            countrytype = []
            countrytype[0] = country.total_confirmed_cases
            countrytype[1] = country.total_deaths
            countrytype[2] = country.total_recovered
            
            return {'country': country.country_name, 'state': country.states, 
            'type': country.total_confirmed_cases, 'date': country.dates}
    jsonField_country = json.dumps(load_csv.Country, default=encoder_country)
    print()
    print(json)


#def informationList(self, request):
 #   if request.method == 'GET':
  #      data = Country.objects.all()
        #or
        #data =  [ {"country: ": CountrySerializer.country_name, 
        #"states:": CountrySerializer.states} 
        #for data in Country.objects.all() ]
        #return Response(data)

        #country_query = request.GET.get('country_name')
        #state_query = request.GET.get('state')
        #date_query = request.GET.get('date')

        #if country_query != '' and 
   #     serializer = CountrySerializer(data, context={'request': request}, many=True)

    #    return Response(serializer.data)

#    elif request.method == 'POST':
#        serializer = CountrySerializer(data=request.data)
#        if serializer.is_valid():
            #serializer.save()
#            return Response(status=status.HTTP_201_CREATED)
            
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
