from django.urls import path
from .views import *

# # in myproject/backend/backend.py or myproject/api/api.py
from .data_layer.load_csv import *

urlpatterns = [
	path("SampleEndpoint", SampleEndpoint.as_view()),
	path("countries/", CountriesEndpoint.as_view()),
	path("AddEndpoint", AddEndpoint.as_view()),
	path("EditEndpoint", EditEndpoint.as_view()),
	path("DeleteEndpoint", DeleteEndpoint.as_view()),
	path("BackupEndpoint", BackupEndpoint.as_view()),
  	path('QueryEndpoint',QueryEndpoint.as_view())
]

data_layer = DataLayer()
data_layer.initLoadCSV("api/data/archive/Copy_covid_19_data.csv")
