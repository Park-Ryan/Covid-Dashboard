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
	path("CountryTopDeaths", CountryTopDeathsEndpoint.as_view()),
	path("StateTopCases", StateTopCasesEndpoint.as_view()),
	path("StateTopDeaths", StateTopDeathsEndpoint.as_view()),
	path("StateTopRecovery", StateTopRecoveryEndpoint.as_view()),
	path("QueryEndpoint", QueryEndpoint.as_view()),
	path("AnalyticsEndpoint", AnalyticsEndpoint.as_view()),
]

data_layer = DataLayer()
data_layer.initLoadCSV("api/data/archive/covid_19_data.csv")
data_layer.initTotals()
data_layer.init_top_5_country()
