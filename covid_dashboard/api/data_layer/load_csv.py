import json
import csv
from typing import OrderedDict

# Every single province/state after merging all the dates togethers
# TODO: find a way for state searches and states' total confirmed cases and etc..
class country:
	def __init__(self, country_name):
		self.country = country_name
		self.states = []
		self.total_confirmed_cases = 0
		self.total_deaths = 0
		self.total_recovered = 0
		self.dates = {}
		# Ex.
		# self.dates = {
		# 	"1/22/2020": {"confirmed_cases": 0, "deaths": 0, "recovered": 0},
		# 	"1/23/2020": {"confirmed_cases": 0, "deaths": 0, "recovered": 0},
		# 	"1/24/2020": {"confirmed_cases": 0, "deaths": 0, "recovered": 0},
		# 	"1/25/2020": {"confirmed_cases": 0, "deaths": 0, "recovered": 0},
		# 	"1/26/2020": {"confirmed_cases": 0, "deaths": 0, "recovered": 0},
		# }

	# returns object in json format
	def info(self):
		return {
			"Country/Region": self.country,
			"Province/State": self.state,
			"Total Confirmed": self.total_confirmed_cases,
			"Total Deaths": self.total_deaths,
			"Total Recovered": self.total_recovered,
		}


# key => state/province
# value => name of state
# state[state/province, state_name]


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
		for key, value in countries_dict.items():
			print(value, "\n")
			break


data_layer = data_layer()
data_layer.initLoadCSV("covid_dashboard/api/data/archive/covid_19_data.csv")
# data_layer.load_json()
# print(data_layer.countries_list)
