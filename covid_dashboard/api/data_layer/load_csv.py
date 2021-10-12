import json
import csv
from typing import Dict, OrderedDict


class Date:
	def __init__(self, date: str, confirmed, deaths, recovered):
		self.date = date
		self.confirmed = confirmed
		self.deaths = deaths
		self.recovered = recovered

	def __repr__(self):
		return "Date: % s, Confirmed: % s, Deaths: % s, Recovered: % s" % (
			self.date,
			self.confirmed,
			self.deaths,
			self.recovered,
		)

	def reprJSON(self):
		return dict(
			date=self.date,
			confirmed=self.confirmed,
			deaths=self.deaths,
			recovered=self.recovered,
		)


class State:
	def __init__(self, state_name, country_name):
		self.state_name = state_name
		self.country_name = country_name
		self.total_confirmed_cases = 0
		self.total_deaths = 0
		self.total_recovered = 0
		self.dates = {}
		self.is_converted_to_json = False

	def __repr__(self):
		return "% s, dates: %s" % (self.state_name, self.dates)

	def __eq__(self, other):
		return self.state_name == other.state_name

	def reprJSON(self):
		if not self.is_converted_to_json:
			for k, v in self.dates.items():
				self.dates[k] = v.reprJSON()

			self.is_converted_to_json = True

		return dict(
			country=self.country_name,
			state=self.state_name,
			total_confirmed=self.total_confirmed_cases,
			total_deaths=self.total_deaths,
			total_recovered=self.total_recovered,
			dates=self.dates,
		)


# Every single province/state after merging all the dates togethers
# TODO: find a way for state searches and states' total confirmed cases and etc..
class Country:
	def __init__(self, country_name):
		self.country_name = country_name
		self.states = {}
		self.total_confirmed_cases = 0
		self.total_deaths = 0
		self.total_recovered = 0
		# Some countries don't have a state/province, but if they do we put it into the states list and leave dates in country empty
		# Stores date objs
		self.dates = {}

	def __repr__(self):
		return "country name is % s, states are % s, dates are % s" % (
			self.country_name,
			self.states,
			self.dates,
		)

	# returns object in json format
	def info(self):
		return {
			"Country/Region": self.country_name,
			"Province/State": self.states,
			"Total Confirmed": self.total_confirmed_cases,
			"Total Deaths": self.total_deaths,
			"Total Recovered": self.total_recovered,
		}

	def reprJSON(self):
		return dict(
			country=self.country_name,
			states=self.states,
			total_confirmed=self.total_confirmed_cases,
			total_deaths=self.total_deaths,
			total_recovered=self.total_recovered,
			dates=self.dates,
		)


class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		if hasattr(obj, "reprJSON"):
			return obj.reprJSON()
		else:
			return json.JSONEncoder.default(self, obj)


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

# TODO: add range based search
class DataLayer:
	def __init__(self):
		# key = country_name : value = country_obj
		self.countries_data = {}
		# helper list to help us sort
		self.countries_list = []
		# holds all the country objects created(kinda like a bootleg database)
		self.country_objects = []

	def test(self):
		print("works")

	def load_json(self):
		# Testing relative path stuff
		# import os

		# cwd = os.getcwd()  # Get the current working directory (cwd)
		# files = os.listdir(cwd)  # Get all the files in that directory
		# print("Files in %r: %s" % (cwd, files))

		with open("api/data_layer/countries.json") as file:
			data = json.load(file)

		self.countries_list = data["Countries/Regions"]
		# print(self.countries_list)

	def loadCSV(self, csv_name: str):
		countries_dict = {}
		self.load_json()
	
		for country in self.countries_list:
			countries_dict[country] = []
		
		with open(csv_name, "r") as infile:	
			for line in infile.readlines():
				row_values = line.split(',')
				row_values[7] = row_values[7].strip("\n")
				if row_values[3] in countries_dict:
					countries_dict[row_values[3]].append(row_values)
		
		for key, value in countries_dict.items():
			#country_obj => is a tmp country object to pass into function
			country_obj = Country(key)

			# state is a dict
			for state in value:
				# print(state)
				# convert the date and cases into a date obj
				date_obj = Date(state[1], state[5], state[6], state[7])
				temp_state = State(state[2], key)
				# Add the dates to the states that already exist
				if state[2] in country_obj.states:
					country_obj.states[state[2]].dates.append(date_obj)

				elif state[2] not in country_obj.states:
					temp_state.dates.append(date_obj)
					country_obj.states[state[2]] = temp_state
					# print(country_obj.states)

				# if there is no value for state/province then add to country obj
				elif state[2] == "":
					country_obj.dates.append(date_obj)
			
			self.countries_data[key] = country_obj
			# self.country_objects.append(country_obj)	

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
		# first check if states exist in the list
		# if it does append and country.states.dates

		# Objects Conversion part
		for key, value in countries_dict.items():
			# country_obj => is a tmp country object to pass into function
			country_obj = Country(key)

			# state is a dict
			for state in value:
				# print(state)
				# convert the date and cases into a date obj
				date_obj = Date(
					state["ObservationDate"], state["Confirmed"], state["Deaths"], state["Recovered"]
				)
				temp_state = State(state["Province/State"], key)
				# Add the dates to the states that already exist
				if state["Province/State"] in country_obj.states:
					country_obj.states[state["Province/State"]].dates[
						state["ObservationDate"]
					] = date_obj
					# country_obj.states[state["Province/State"]].dates.append(date_obj)

				elif state["Province/State"] not in country_obj.states:
					# temp_state.dates.append(date_obj)
					temp_state.dates[state["ObservationDate"]] = date_obj
					country_obj.states[state["Province/State"]] = temp_state
					# print(country_obj.states)

				# if there is no value for state/province then add to country obj
				elif state["Province/State"] == "":
					# country_obj.dates.append(date_obj)
					country_obj.dates[state["ObservationDate"]] = date_obj

			self.countries_data[key] = country_obj
			# self.country_objects.append(country_obj)

		print("Finish loading csv")

	# Returns the lists of all countries
	def get_countries(self):
		return self.countries_data


# data_layer = data_layer()
# data_layer.initLoadCSV("covid_dashboard/api/data/archive/covid_19_data.csv")
# countries = data_layer.get_countries()

# # Testing
# for date in countries["US"].states["California"].dates:
# 	print(date, "\n")


# data_layer.load_json()
# print(data_layer.countries_list)