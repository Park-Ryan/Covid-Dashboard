from datetime import timedelta
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .util import (
	Backup_Csv,
	Get_Filtered_Data,
	Create_Csv,
	Delete_Csv,
	Get_Top_5_Countries_Deaths,
	Get_Top_5_States_Cases,
	Get_Top_5_States_Deaths,
	Get_Top_5_States_Recovered,
	Update_Csv,
)
import time
from .util import *
from datetime import datetime
from queue import PriorityQueue

# from covid_dashboard.api.data_layer.load_csv import Country

# from .serializers import *
import json

# # in myproject/backend/backend.py or myproject/api/api.py
# from .data_layer.load_csv import *

# # import the data layer object to the views
# from .apps import *


pct_analytics = {}
avg_analytics = {}
std_analytics = {}

incremental_analytic = {}
did_change = False

default_days = 7


class SampleEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data
		output_payload = None

		output_payload = Reverse_String(input_payload)

		return Response(output_payload, status=status.HTTP_200_OK)


# for testing
class CountriesEndpoint(APIView):
	def get(self, request):
		# import the data layer object to the views
		from .urls import data_layer, ComplexEncoder

		countries = data_layer.get_countries()
		# print(countries["US"].states["California"].dates["01/21/2021"])

		# results = CountrySerializer(countries, many=True).data
		# this is returning str instead of json literal
		# double encoding happening
		result = json.dumps(
			# 	# countries["US"].states["California"].dates["01/21/2021"].reprJSON()
			countries["US"].states["California"],
			cls=ComplexEncoder,
		)
		countries["US"].states["California"].dates

		# print(countries["US"].states["California"].dates["01/21/2021"])
		# return Response(countries["US"].states["California"].reprJSON())
		return Response(countries["Taiwan"].reprJSON())


# TODO: Refactor to not call get analytics 3 times since we get all 3 types in one go
# TODO: its slow when analytics for all states, optimize later
# # TODO: maybe a better format for json as well but later
# class AnalyticsEndpoint(APIView):
# 	from .urls import data_layer

# 	"""
# 		TODO: We need to store the analytics after each computation
# 		IDEA:
# 			1. Create a separate dict for each if statement below
# 				- This allows for quicker individual searching possibly?

# 	"""
# 	#If statement 5: Country, no state, no date -> from beginning date to end [{"State" : [confirmed, deaths, recovered]}, ...]
# 	#this dictionary will store the info

# 	default_days = 7
# 	types = ["Confirmed", "Deaths", "Recovered"]
# 	input_payload = self.request.data
# 	payload = []

# 	country_query = input_payload["payload"]["countryVal"]
# 	state_query = input_payload["payload"]["stateVal"]
# 	type_query = input_payload["payload"]["typeVal"]
# 	date_query = input_payload["payload"]["dateVal"]

# 		"""
# 		Cases:
# 			1. Input country, state, and two dates ->  [{"State" : [confirmed, deaths, recovered]}]
# 			2. Country, state, one date ->  [{"State" : [confirmed, deaths, recovered]}]
# 			3. Country, state, no date -> from beginning date to end  [{"State" : [confirmed, deaths, recovered]}]
# 			4. Country, no state, two dates -> [{"State" : [confirmed, deaths, recovered]}, ...]
# 			5. Country, no state, one date -> [{"State" : [confirmed, deaths, recovered]}, ...]
# 			6. Country, no state, no date -> from beginning date to end [{"State" : [confirmed, deaths, recovered]}, ...]

# 		"""

# 		# TESTING, take this out when actual args get passed
# 		# country_query = "US"
# 		# state_query = ""
# 		# type_query = ""
# 		# date_query = ""
# 		end_date_query = ""
# 		# default is to get the past 7 days if end date query is empty
# 		# end_date_query = input_payload["payload"]["dateVal"]

# 		# TODO: Check if date is valid/exists within database

# 		# if end date is empty str, we need end date to be the starting date
# 		# bc its the previous last 7 days
class AnalyticsEndpoint(APIView):
	def post(self, request, format=None):
		from .urls import data_layer

		default_days = 7
		input_payload = self.request.data
		payload = []

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		"""
			Cases:
				1. Input country, state, and two dates ->  [{"State" : [confirmed, deaths, recovered]}]
				2. Country, state, one date ->  [{"State" : [confirmed, deaths, recovered]}]
				3. Country, state, no date -> from beginning date to end  [{"State" : [confirmed, deaths, recovered]}]
				4. Country, no state, two dates -> [{"State" : [confirmed, deaths, recovered]}, ...]
				5. Country, no state, one date -> [{"State" : [confirmed, deaths, recovered]}, ...]
				6. Country, no state, no date -> from beginning date to end [{"State" : [confirmed, deaths, recovered]}, ...]
			
			"""

		# TESTING, take this out when actual args get passed
		# country_query = "US"
		# state_query = ""
		# type_query = ""
		# date_query = ""
		end_date_query = ""
		# default is to get the past 7 days if end date query is empty
		# end_date_query = input_payload["payload"]["dateVal"]

		# TODO: Check if date is valid/exists within database
		start_time = time.time()
		payload = query_selector(country_query, state_query, date_query, end_date_query)
		elapsed_time = time.time() - start_time
		print("Time elapsed for analytic endpoint is : " + str(elapsed_time) + " seconds")
		# if end date is empty str, we need end date to be the starting date
		# bc its the previous last 7 days

		return Response(payload, status=status.HTTP_200_OK)


def update_Value(country_query, state_query, type_query, amount_query):
	from .urls import data_layer

	start_time = time.time()

	total_type_query = "Total_" + type_query
	print("total type: ", total_type_query)
	# NOTE: reprJSON is read only
	country_total = data_layer.countries_data.get(country_query).reprJSON()[
		total_type_query
	]
	state_total = (
		data_layer.countries_data.get(country_query)
		.states.get(state_query)
		.reprJSON()[total_type_query]
	)

	total_days = 493 + 1
	tmp_total = (incremental_analytic[country_query][0]["averages"]) * total_days
	average = (tmp_total + float(amount_query)) / total_days
	variance = pow(incremental_analytic[country_query][0]["std"], 2)
	variance = variance + pow((float(amount_query) - average), 2)
	variance /= total_days
	std = math.sqrt(variance)
	percentages = (float(state_total) / float(country_total)) * 100
	incremental_analytic[country_query][0]["averages"] = average
	incremental_analytic[country_query][0]["std"] = std
	incremental_analytic[country_query][0]["percentages"] = percentages
	elapsed_time = time.time() - start_time
	print("Time elapsed for update endpoint is : " + str(elapsed_time) + " seconds")


def query_selector(country_query, state_query, date_query, end_date_query):
	from .urls import data_layer

	payload = []
	if state_query and date_query and not end_date_query:
		temp_date_obj = datetime.strptime(date_query, "%m/%d/%Y")
		# subtracting 7 days to current date,
		# TODO: Default is 7 days, make a var to make it easily editable
		# handles case if near the end of the month ex. day 30 - 7 = 03/23/2021
		temp_date_obj -= timedelta(days=default_days)

		start_date_query = temp_date_obj.strftime("%m/%d/%Y")
		payload.extend(
			Get_Analytics(country_query, state_query, start_date_query, date_query).split()
		)
		print(payload)
	elif (
		state_query and not date_query and not end_date_query
	):  # no dates return all days for that one state
		# Get earliest available date & last date
		date_query = list(
			data_layer.countries_data.get(country_query).states.get(state_query).dates.keys()
		)[0]
		end_date_query = list(
			data_layer.countries_data.get(country_query).states.get(state_query).dates.keys()
		)[-1]

		payload.extend(Get_Analytics(country_query, state_query, date_query, end_date_query))
	# Case: no state, but given date range
	elif (
		not state_query and date_query and end_date_query
	):  # if state empty return all states

		for state_key in data_layer.countries_data.get(country_query).states.keys():
			# TODO: Check if date is valid/exists within database, if it does not skip/continue? this state
			# NOTE: What if user inputs the same date for both start and end?
			# TODO: Check if date is valid/exists within database, if it does not skip/continue? this state
			if (
				date_query
				not in data_layer.countries_data.get(country_query)
				.states.get(state_key)
				.dates.keys()
			):
				# print("start: ", date_query, "end:", end_date_query)
				continue

			payload.extend(Get_Analytics(country_query, state_key, date_query, end_date_query))
	elif (
		not state_query and date_query and not end_date_query
	):  # if state empty return all states
		print("NO STATE, DATE")
		for state_key in data_layer.countries_data.get(country_query).states.keys():

			temp_date_obj = datetime.strptime(date_query, "%m/%d/%Y")
			temp_date_obj -= timedelta(days=default_days)
			start_date_query = temp_date_obj.strftime("%m/%d/%Y")

			# TODO: Check if date is valid/exists within database, if it does not skip/continue? this state
			if (
				start_date_query
				not in data_layer.countries_data.get(country_query)
				.states.get(state_key)
				.dates.keys()
			):
				# print("start: ", start_date_query, "end:", date_query)
				continue

			payload.extend(Get_Analytics(country_query, state_key, start_date_query, date_query))
			# print(payload)

	elif not state_query and not date_query and not end_date_query:
		# print("IN NO STATE, NO START DATE, NO END DATE, CASE")
		start_time = time.time()

		if country_query not in incremental_analytic.keys():
			print("Reached inside only country for loop")
			for state_key in data_layer.countries_data.get(country_query).states.keys():

				# Get earliest available date & last date
				date_query = list(
					data_layer.countries_data.get(country_query).states.get(state_key).dates.keys()
				)[0]
				end_date_query = list(
					data_layer.countries_data.get(country_query).states.get(state_key).dates.keys()
				)[-1]

				# print("start: ", date_query, "end:", end_date_query, "\n")

				# if both dates are the same, then skip bc its not important
				if date_query == end_date_query:
					continue

				payload.extend(Get_Analytics(country_query, state_key, date_query, end_date_query))

		incremental_analytic[country_query] = payload
		elapsed_time = time.time() - start_time
		print("Time elapsed for analytic endpoint is : " + str(elapsed_time) + " seconds")
		payload = incremental_analytic[country_query]

	else:  # Regular process
		payload.extend(Get_Analytics(country_query, state_query, date_query, end_date_query))
	# print(payload)

	return payload


# end of death analytics


# def informationList(self, request):
#   if request.method == 'GET':
#      data = Country.objects.all()
# or
# data =  [ {"country: ": CountrySerializer.country_name,
# "states:": CountrySerializer.states}
# for data in Country.objects.all() ]
# return Response(data)

# country_query = request.GET.get('country_name')
# state_query = request.GET.get('state')
# date_query = request.GET.get('date')

# if country_query != '' and
#     serializer = CountrySerializer(data, context={'request': request}, many=True)

#    return Response(serializer.data)

#    elif request.method == 'POST':
#        serializer = CountrySerializer(data=request.data)
#        if serializer.is_valid():
# serializer.save()
#            return Response(status=status.HTTP_201_CREATED)


class QueryEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]
		start_time = time.time()
		payload = Get_Filtered_Data(country_query, state_query, type_query, date_query)
		elapsed_time = time.time() - start_time
		print("Time elapsed for query endpoint is : " + str(elapsed_time) + " seconds")
		return Response(payload, status=status.HTTP_200_OK)


class AddEndpoint(APIView):
	def post(self, request, format=None):
		input_payload = self.request.data

		# TODO : Implement backend logic

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]
		amount_query = input_payload["payload"]["amountVal"]
		start_time = time.time()
		payload = Create_Csv(country_query, state_query, type_query, date_query, amount_query)
		elapsed_time = time.time() - start_time
		print("Time elapsed for add endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)


class EditEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		# TODO : Implement backend logic
		did_change = True

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]
		amount_query = input_payload["payload"]["amountVal"]

		start_time = time.time()
		payload = Update_Csv(country_query, state_query, type_query, date_query, amount_query)
		print("Did change bool:")
		print(did_change)
		if did_change:
			update_Value(country_query, state_query, type_query, amount_query)
			did_change = False
		elapsed_time = time.time() - start_time
		print("Time elapsed for edit endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)


class DeleteEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		# TODO : Implement backend logic

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]
		amount_query = input_payload["payload"]["amountVal"]

		start_time = time.time()
		payload = Delete_Csv(country_query, state_query, date_query)
		elapsed_time = time.time() - start_time
		print("Time elapsed for delete endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)


class BackupEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		# TODO : Implement backend logic

		start_time = time.time()
		# Backup doesn't require any data to be passed in from the frontend

		payload = Backup_Csv("api/data/archive/Copy_covid_19_data.csv")
		elapsed_time = time.time() - start_time
		print("Time elapsed for backup endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)


class CountryTopDeathsEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_Countries_Deaths()
		elapsed_time = time.time() - start_time
		print(
			"Time elapsed for country top deaths endpoint is : " + str(elapsed_time) + " seconds"
		)

		return Response(payload, status=status.HTTP_200_OK)


class StateTopCasesEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_States_Cases()
		elapsed_time = time.time() - start_time
		print(
			"Time elapsed for state top cases endpoint is : " + str(elapsed_time) + " seconds"
		)

		return Response(payload, status=status.HTTP_200_OK)


class StateTopDeathsEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_States_Deaths()
		elapsed_time = time.time() - start_time
		print(
			"Time elapsed for state top deaths endpoint is : " + str(elapsed_time) + " seconds"
		)

		return Response(payload, status=status.HTTP_200_OK)


class StateTopRecoveryEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_States_Recovered()
		elapsed_time = time.time() - start_time
		print(
			"Time elapsed for state top recovery endpoint is : " + str(elapsed_time) + " seconds"
		)

		return Response(payload, status=status.HTTP_200_OK)
