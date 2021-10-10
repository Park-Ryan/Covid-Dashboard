import json
import csv
from typing import Dict, OrderedDict

class Date: 
	def __init__(self, date: str, recovered, cases, deaths):
		self.date = date
		self.recovered = recovered
		self.cases = cases
		self.deaths = deaths

class State:
	def __init__(self, state_name, country_name):
		self.state_name = state_name
		self.country_name = country_name
		self.total_confirmed_cases = 0
		self.total_deaths = 0
		self.total_recovered = 0
		self.dates = []


# Every single province/state after merging all the dates togethers
# TODO: find a way for state searches and states' total confirmed cases and etc..
class Country:
	def __init__(self, country_name):
		self.country_name = country_name
		self.states = []
		self.total_confirmed_cases = 0
		self.total_deaths = 0
		self.total_recovered = 0
		# Some countries don't have a state/province, but if they do we put it into the states list and leave dates in country empty
		# Stores date objs
		self.dates = []

	# returns object in json format
	def info(self):
		return {
			"Country/Region": self.country,
			"Province/State": self.state,
			"Total Confirmed": self.total_confirmed_cases,
			"Total Deaths": self.total_deaths,
			"Total Recovered": self.total_recovered,
		}



# Group all the "provice/states" that have the same name
# [
# 	OrderedDict(
# 		[
# 			("SNo", "2"),
# 			("ObservationDate", "01/22/2020"),
# 			("Province/State", "Beijing"),
# 			("Country/Region", "Mainland China"),
# 			("Last Update", "1/22/2020 17:00"),
# 			("Confirmed", "14.0"),
# 			("Deaths", "0.0"),
# 			("Recovered", "0.0"),
# 		]
# 	),
# 	OrderedDict(
# 		[
# 			("SNo", "42"),
# 			("ObservationDate", "01/23/2020"),
# 			("Province/State", "Beijing"),
# 			("Country/Region", "Mainland China"),
# 			("Last Update", "1/22/2020 17:00"),
# 			("Confirmed", "20.0"),
# 			("Deaths", "0.0"),
# 			("Recovered", "0.0"),
# 		]
# 	),
# ]


class data_layer:
	def __init__(self):
		# key = country_name : value = country_obj
		self.countries_data = {}
		# helper list to help us sort
		self.countries_list = []
		# holds all the country objects created(kinda like a bootleg database)
		self.country_objects = []

	def load_json(self):
		with open("covid_dashboard/api/data_layer/countries.json") as file:
			data = json.load(file)

		self.countries_list = data["Countries/Regions"]
		# print(self.countries_list)

	def initLoadCSV(self, csv_name: str):
		countries_dict = {}
		self.load_json()

		# loop thru countries list and make a key(country name), value([OrderedDict()])
		for country in self.countries_list:
			countries_dict[country] = []

		with open(csv_name, newline="") as csvfile:
			reader = csv.DictReader(csvfile, delimiter=",")
			for row in reader:
				# if the value of country is in the countries dict,
				# take the value and use it as a key in the countries dict and add all the countries with that value into the list
				if row["Country/Region"] in countries_dict:
					countries_dict[row["Country/Region"]].append(row)

			# 	print(reader["SNo"])  # prints the whole SNo column
			# # since dictreader only allows iterability
			# row = next(reader)  # goes next and keeps pointer position
			# print(row)
			# print(countries_dict)

		# iterate thru all the keys and turn all the values into a country object
		# value is a list containing all the json data for a country
		#first check if states exist in the list
		#if it does append and country.states.dates
		
		# Objects Conversion part
		for key, value in countries_dict.items():
			#country_obj => is a tmp country object to pass into function
			country_obj = Country(key)
			# state is a dict
			for state in value:
				# print(state)
				# convert the date and cases into a date obj
				date_obj = Date(state["ObservationDate"], state["Confirmed"], state["Deaths"], state["Recovered"])
				# if there is no value for state/province then add to country obj
				if not state["Province/State"]:
					country_obj.dates.append(Date(state["ObservationDate"], state["Confirmed"], state["Deaths"], state["Recovered"]))
				if state["Province/State"] not in country_obj.states:
					country_obj.states.append(State(state["Province/State"], key))
					# print(country_obj.states)
			
			
				
			self.country_objects.append(country_obj)	
		
	def return_object(self):
		return self.country_objects
		
		
		# for	x in self.country_objects:
		# 	for state in x.states:
		# 		print(state.state_name)
		#print(self.country_objects[0].states[0].state)		


data_layer = data_layer()
data_layer.initLoadCSV("covid_dashboard/api/data/archive/covid_19_data.csv")
data_layer.return_object()
# data_layer.load_json()
# print(data_layer.countries_list)
