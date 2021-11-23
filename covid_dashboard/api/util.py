from os import stat
from .data_layer.load_csv import *
import json
import copy
from array import array
import math
import numpy as np
from queue import PriorityQueue

did_change = False

def Reverse_String(dict):

	payload = dict["payload_bus"]

	payload = str(payload[::-1])

	payload = payload.replace("'", '"')

	return payload


def Get_Top_5_Countries_Deaths():
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()
	country_deaths = 0.0
	payload = []
	tmp_list = []
	death_dict = {}
	state_max = 0.0
	empty = ""

	for country_key, country_obj in tmp_countries_list.items():
		country_deaths = 0.0
		for state_key, state_obj in country_obj.states.items():
			death_list = []  # deaths list per state
			for date_obj in state_obj.dates.values():
				tmp_list = date_obj.deaths
				# date_obj.deaths returns a list of strings containing all the deaths
				# then going to use this for loop convert that to a float to use the max
				for line in tmp_list.splitlines():
					# splits the in the tmp_list to a float
					death_list.append(float(line))
				# at the end of the conversion you now have a list of float values for the state.dates
			state_max = max(death_list)  # using the max of the list of float for states
			country_deaths += state_max

		death_dict[country_key] = country_deaths

	death_dict = dict(sorted(death_dict.items(), key=lambda item: item[1], reverse=True))
	death_dict_keys = death_dict.keys()
	top_five_keys = list(death_dict_keys)[:5]
	death_dict_values = death_dict.values()
	top_five_values = list(death_dict_values)[:5]

	# for i in range(0, 5):
	# 	payload.append(
	# 		{
	# 			"Country": top_five_keys[i],
	# 			"State": empty,
	# 			"Date": empty,
	# 			"Types": {"Confirmed": empty, "Deaths": top_five_values[i], "Recovered": empty},
	# 		}
	# 	)


	for i in range(0, 5):
		payload.append(
			{
				"Country":data_layer.top_5_death_pq.queue[i][1].country_name,
				"State": empty,
				"Date": empty,
				"Types": {"Confirmed": empty, "Deaths": data_layer.top_5_death_pq.queue[i][1].total_deaths, "Recovered": empty},
			}
		)
	return payload

#not using currently
def Get_Top_5_States_Cases():
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	payload = []
	tmp_list = []
	case_dict = {}
	state_max = 0.0
	empty = ""

	for country_key, country_obj in tmp_countries_list.items():
		state_max = 0.0
		for state_key, state_obj in country_obj.states.items():
			case_list = []  # case list per state
			for date_obj in state_obj.dates.values():
				tmp_list = date_obj.confirmed
				# date_obj.deaths returns a list of strings containing all the deaths
				# then going to use this for loop convert that to a float to use the max
				for line in tmp_list.splitlines():
					# splits the in the tmp_list to a float
					case_list.append(float(line))
				# at the end of the conversion you now have a list of float values for the state.dates
			state_max = max(case_list)  # using the max of the list of float for states
			case_dict[state_key] = state_max

	# sort the dict then only need to grab the top 5 values
	case_dict = dict(sorted(case_dict.items(), key=lambda item: item[1], reverse=True))
	case_dict_keys = case_dict.keys()
	top_five_keys = list(case_dict_keys)[:5]
	case_dict_values = case_dict.values()
	top_five_values = list(case_dict_values)[:5]

	for i in range(0, 5):
		payload.append(
			{
				"Country": empty,
				"State": top_five_keys[i],
				"Date": empty,
				"Types": {"Confirmed": top_five_values[i], "Deaths": empty, "Recovered": empty},
			}
		)
	#print(payload)
	return payload

#not using
def Get_Top_5_States_Deaths():
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()
	# TotalArray = []
	# total_deaths = 0.0
	# finalTotal = []

	# for country_key, country_obj in tmp_countries_list.items():
	# 	if stateFilter in country_obj.states:
	# 		for date_key, date_obj in country_obj.states[stateFilter].dates.items():
	# 				total_deaths += float((tmp_countries_list[country_key].states[stateFilter].dates[date_key].reprJSON()["Deaths"]))

	# 	TotalArray.append(total_deaths)
	# for x in range(5):
	# 	finalTotal.append(max(TotalArray))
	# 	TotalArray.remove(max(TotalArray))

	payload = []
	tmp_list = []
	case_dict = {}
	state_max = 0.0
	empty = ""

	for country_key, country_obj in tmp_countries_list.items():
		state_max = 0.0
		for state_key, state_obj in country_obj.states.items():
			case_list = []  # case list per state
			for date_obj in state_obj.dates.values():
				tmp_list = date_obj.deaths
				# date_obj.deaths returns a list of strings containing all the deaths
				# then going to use this for loop convert that to a float to use the max
				for line in tmp_list.splitlines():
					# splits the in the tmp_list to a float
					case_list.append(float(line))
				# at the end of the conversion you now have a list of float values for the state.dates
			state_max = max(case_list)  # using the max of the list of float for states
			case_dict[state_key] = state_max

	# sort the dict then only need to grab the top 5 values
	case_dict = dict(sorted(case_dict.items(), key=lambda item: item[1], reverse=True))
	case_dict_keys = case_dict.keys()
	top_five_keys = list(case_dict_keys)[:5]
	case_dict_values = case_dict.values()
	top_five_values = list(case_dict_values)[:5]

	for i in range(0, 5):
		payload.append(
			{
				"Country": empty,
				"State": top_five_keys[i],
				"Date": empty,
				"Types": {"Confirmed": empty, "Deaths": top_five_values[i], "Recovered": empty},
			}
		)
	#print(payload)
	return payload


#not using
def Get_Top_5_States_Recovered():
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()
	# TotalArray = {}
	# total_deaths = 0.0

	# for country_key, country_obj in tmp_countries_list.items():
	# 	if stateFilter in country_obj.states:
	# 		for date_key, date_obj in country_obj.states[stateFilter].dates.items():
	# 				total_deaths += float((tmp_countries_list[country_key].states[stateFilter].dates[date_key].reprJSON()["Recovered"]))

	# 	TotalArray[country_key] = total_deaths

	# print(max(TotalArray.values()))
	payload = []
	tmp_list = []
	case_dict = {}
	state_max = 0.0
	empty = ""

	for country_key, country_obj in tmp_countries_list.items():
		state_max = 0.0
		for state_key, state_obj in country_obj.states.items():
			case_list = []  # case list per state
			for date_obj in state_obj.dates.values():
				tmp_list = date_obj.recovered
				# date_obj.deaths returns a list of strings containing all the deaths
				# then going to use this for loop convert that to a float to use the max
				for line in tmp_list.splitlines():
					# splits the in the tmp_list to a float
					case_list.append(float(line))
				# at the end of the conversion you now have a list of float values for the state.dates
			state_max = max(case_list)  # using the max of the list of float for states
			case_dict[state_key] = state_max

	# sort the dict then only need to grab the top 5 values
	case_dict = dict(sorted(case_dict.items(), key=lambda item: item[1], reverse=True))
	case_dict_keys = case_dict.keys()
	top_five_keys = list(case_dict_keys)[:5]
	case_dict_values = case_dict.values()
	top_five_values = list(case_dict_values)[:5]

	for i in range(0, 5):
		payload.append(
			{
				"Country": empty,
				"State": top_five_keys[i],
				"Date": empty,
				"Types": {"Confirmed": empty, "Deaths": empty, "Recovered": top_five_values[i]},
			}
		)
	#print(payload)
	return payload


# def Copy_Csv(self, pathOfOriginal):

# Backup CSV
def Backup_Csv(path):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	# print(tmp_countries_list["US"])

	SNo = ""
	LastUpdate = ""
	csv_country = ""
	csv_state = ""
	date = ""
	confirmed = ""
	deaths = ""
	recovered = ""
	with open(path, "w") as outfile:
		for countryKey, country in tmp_countries_list.items():
			csv_country = countryKey
			for stateKey, state in country.states.items():
				csv_state = stateKey
				for dates in state.dates.values():
					date = dates.date
					confirmed = dates.confirmed
					deaths = dates.deaths
					recovered = dates.recovered
					tmp_join = [SNo, date, csv_state, csv_country, date, confirmed, deaths, recovered]
					tmp_string = ",".join(tmp_join)
					tmp_string += "\n"
					outfile.write(tmp_string)


# SNo,ObservationDate,Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered
# Create(Country: USA, State: California, Confirmed : 0, Deaths: 0, Recovered: 0, Date: 9/11/2021)
def Create_Csv(country, state, type, date, amount):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()
	# if country is not in the tmp list
	# then we can just append to the dictionary becasuse that country doesn't exist
	# else it exists
	# then use that country as a key and append to that

	# this checks if the country is in the country list dictionary
	# if country in tmp_countries_list:
	# date_obj is a date object that will be added to the country list
	# Since function only takes in specified input then we have to check
	# which type it is. After entering specified amount for type then
	# make the other 2 types default 0
	if date in tmp_countries_list[country].states[state].dates:

		print("Create Exist. Go To Edit Instead.")
	else:

		if type == "Deaths":
			date_obj = Date(date, "0", str(amount), "0")
		elif type == "Confirmed":
			date_obj = Date(date, str(amount), "0", "0")
		elif type == "Recovered":
			# then make a date object to add to the country object
			date_obj = Date(date, "0", "0", str(amount))
			# sets country object dates to the date object
		tmp_countries_list[country].states[state].dates[date] = date_obj
		
		# finally add the country object to the countries list
		# based on the country parameter from user

	# else:
	# 	#the country doesn't exist  so need to make a country object
	# 	country_obj = Country(country)
	# 	if type == "Deaths":
	# 		date_obj = Date(date,"0", str(amount), "0")
	# 	elif type == "Confirmed":
	# 		date_obj = Date(date,str(amount), "0", "0")
	# 	elif type == "Recovered":
	# 		#then make a date object to add to the country object
	# 		date_obj = Date( date,"0", "0", str(amount))
	# 		#sets country object dates to the date object
	# 	country_obj.states[state].dates[date] = date_obj
	# 		#finally add the country object to the countries list
	# 		#based on the country parameter from user
	# 	tmp_countries_list[country] = country_obj

	# back in the load_csv.py
	# will set the countries_data to tmp_countries_list so we can use the updated data
	# print(tmp_countries_list[country].states[state])
	data_layer.set_countries(tmp_countries_list)


# only update the confirmed, deaths, or recovered cases
def Update_Csv(country, state, type, date, value):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()
	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			if date in tmp_countries_list[country].states[state].dates:
				if type == "Deaths":
					# print(tmp_countries_list[country].states[state].dates[date].reprJSON()[type])
					date_obj = Date(
						date,
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Confirmed"],
						str(value),
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Recovered"],
					)
					tmp_countries_list[country].states[state].dates[date] = date_obj
					print("Edit Deaths")
					# print(tmp_countries_list[country].states[state].dates[date].reprJSON()[type])
				elif type == "Recovered":
					date_obj = Date(
						date,
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Confirmed"],
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Deaths"],
						str(value)
					)
					tmp_countries_list[country].states[state].dates[date] = date_obj
					print("Edit Recovered")
				elif type == "Confirmed":
					date_obj = Date(
						date,
						str(value),
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Deaths"],
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Recovered"],
					)
					tmp_countries_list[country].states[state].dates[date] = date_obj
					print("Edit Confirmed")
				else:
					print("Update doesnt work")
			else:
				print("Update couldn't find date")
	data_layer.set_countries(tmp_countries_list)



# type doesn't matter because you're deleting the whole row of values
# i.e for 01/20/2020 you would delete the whole row
def Delete_Csv(country, state, date):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	# this checks if the country is in the country list dictionary
	# for key in tmp_countries_list:
	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			if date in tmp_countries_list[country].states[state].dates:
				# print(tmp_countries_list[country].states[state].dates[date])
				del tmp_countries_list[country].states[state].dates[date]
				# print(tmp_countries_list[country].states[state].dates[date])
				# print(tmp_countries_list)
		else:
			print("State no exist")
	else:
		print("Doesn't exist")


def Get_Filtered_Data(countryFilter, stateFilter, typeFilter, dateFilter):

	# putting payload into array so we can iterate thru and put into table?
	# list of jsons/dicts
	payload = []

	# importing the data layer object so we can use the functions within the method
	from .urls import data_layer

	countries_list = data_layer.get_countries()
	# TODO: none of these account for the dates dictionary inside country!
	# may need to include those later depending on if they contain useful data

	# TODO: might change format of load_csv later to fit a universal json format
	# NOTE: we can make a dynamic table that will change its value based on the json keys

	# NOTE: Aiming for a json format like this
	# {
	#   Country: "Japan"
	#   Date: "09/28/2020"
	#   State: "Tokyo"
	#   Types: {
	#   	Confirmed: "25345.0"
	#   	Deaths: "406.0"
	#   	Recovered: "22647.0"
	# 	}
	# }

	# this accounts for when country is empty or not empty, doesnt matter
	# when no fields are empty
	# return a json of of specific date of a state
	if countryFilter != "" and dateFilter != "" and stateFilter != "":
		if dateFilter in countries_list[countryFilter].states[stateFilter].dates:
			# just return the whole JSON instead of a specific case, let the front end pick which type of case
			payload.append(
				{
					"Country": countryFilter,
					"State": stateFilter,
					"Date": dateFilter,
					# maybe for larger objects like country and state we could use the total cases instead of per date
					"Types": countries_list[countryFilter]
					.states[stateFilter]
					.dates[dateFilter]
					.reprJSON(),
				}
			)
			# print("at country, date, state filled")

	# when country is empty
	# return data for that state and date
	elif countryFilter == "" and stateFilter != "" and dateFilter != "":
		for country_key, country_obj in countries_list.items():
			if stateFilter in country_obj.states:
				# checking if the date is a key within the state's dates dictionary
				if dateFilter in country_obj.states[stateFilter].dates:
					# just return the whole JSON instead of a specific case, let the front end pick which type of case
					payload.append(
						{
							"Country": country_key,  # <- these change
							"State": stateFilter,  # <- these change
							"Date": dateFilter,  # <- when var is given, this will always be the same so you can just slap it there
							"Types": country_obj.states[stateFilter].dates[dateFilter].reprJSON(),
						}
					)

	# when date field is empty
	# in this case, return all dates for a state
	elif countryFilter != "" and stateFilter != "" and dateFilter == "":
		# need date_key bc date filter is empty
		for date_key, date_obj in (
			countries_list[countryFilter].states[stateFilter].dates.items()
		):
			# adding to payload list
			payload.append(
				{
					# we already know the country since every state obj has a country name member within it
					"Country": countries_list[countryFilter].states[stateFilter].country_name,
					"State": stateFilter,
					"Date": date_key,
					"Types": date_obj.reprJSON(),
				}
			)

	# when country and date are empty
	# in this case, return all the dates of that state
	elif countryFilter == "" and stateFilter != "" and dateFilter == "":
		for country_key, country_obj in countries_list.items():
			if stateFilter in country_obj.states:
				for date_key, date_obj in country_obj.states[stateFilter].dates.items():
					# just return the whole JSON instead of a specific case, let the front end pick which type of case
					payload.append(
						{
							"Country": country_key,  # <- these change
							"State": stateFilter,  # <- these change
							"Date": date_key,  # <- when var is given, this will always be the same so you can just slap it there
							"Types": country_obj.states[stateFilter].dates[date_key].reprJSON(),
						}
					)

	# when state and date field is empty(basically all country data) TODO: maybe include country.dates
	# in this case, return all states and dates
	elif countryFilter != "" and stateFilter == "" and dateFilter == "":
		for state_key, state_obj in countries_list[countryFilter].states.items():
			for date_key, date_obj in state_obj.dates.items():
				if date_key in state_obj.dates:  # .dates returns a dictonary
					payload.append(
						{
							"Country": countryFilter,
							"State": state_key,
							"Date": date_key,
							"Types": date_obj.reprJSON(),
						}
					)

	# when state is empty
	# in this case, return all states, but only use the date given
	elif countryFilter != "" and stateFilter == "" and dateFilter != "":
		for state_key, state_obj in countries_list[countryFilter].states.items():
			# checking if the date is a key within the state's dates dictionary
			if dateFilter in state_obj.dates:
				payload.append(
					{
						"Country": countryFilter,
						"State": state_key,
						"Date": dateFilter,
						"Types": state_obj.dates[dateFilter].reprJSON(),
					}
				)

	# when country and state is empty
	# in this case, return all the dates, but only use the date given
	elif countryFilter == "" and stateFilter == "" and dateFilter != "":
		for country_key, country_obj in countries_list.items():
			for state_key, state_obj in country_obj.states.items():
				# checking if the date is a key within the state's dates dictionary
				if dateFilter in state_obj.dates:
					payload.append(
						{
							"Country": country_key,  # <- these change
							"State": state_key,  # <- these change
							"Date": dateFilter,  # <- when var is given, this will always be the same so you can just slap it there
							"Types": state_obj.dates[dateFilter].reprJSON(),
						}
					)

	# print(payload)
	# if payload is empty, no results found / api responsed with nothing
	return payload


# TODO: if state is empty, calc the analytics for country
# if type is empty, calc all the anayltics for each type
# if
def Get_Analytics(country_query, state_query, type_query, start_date, end_date) -> dict:
	from .urls import data_layer

	# passing in cities like chicago / LA, which doesnt have valid dates for 3/30/2021
	dates_dict = data_layer.countries_data.get(country_query).states.get(state_query).dates


	# if date does exist do what?

	# function to get the date range
	type_nums = Get_Date_Range(type_query, start_date, end_date, dates_dict)
	averages = max(type_nums) / len(type_nums)
	variance = sum(pow(x-averages,2) for x in type_nums)
	variance /= (len(type_nums))
	std = math.sqrt(variance)
	
	# print(type_nums)
	# print("this is numpy")
	# a= np.array(type_nums)
	# stds = np.std(a)
	# averagess = np.average(a)
	# print(averagess)
	# print(stds)
	# print("end")
	# print("type nums:", type_nums, "std:", std, "averages:", averages)
	# if start_date == end_date:
	# 	std = type_nums[0]
	# 	averages = type_nums[0]

	# if country and state are given, compute the percentage of covid (confirmed/deaths/recovered) cases
	# to the total country (confirmed/deaths/recovered)
	# TODO: implement methods that initalize the total_deaths, etc, attributes at the start of the server
	# Use those totals to compute the percentages by state_deaths divided by total country deaths
	# three avg
	# 1. all the dates => so daily avg from the beginning of covid
	# 2. one date => prev 7 days to given days = 7 day avg
	# 3. between two dates => avg between those two dates
	"""
		Go into the country
		Iterate through each state
		Sum the totals for each state with the given parameters
		Add that total to the country total
		
	"""
	# change type query str to match Total_ + case
	total_type_query = "Total_" + type_query
	# NOTE: reprJSON is read only
	country_total = data_layer.countries_data.get(country_query).reprJSON()[
		total_type_query
	]
	state_total = (
		data_layer.countries_data.get(country_query)
		.states.get(state_query)
		.reprJSON()[total_type_query]
	)
	# Given only country: country total / global total = percentage
	if not state_query:  # empty state query
		percentages = (
			float(country_total) / float(data_layer.global_total_types.get(total_type_query))
		) * 100
	# Given country and state: state total / country total = percentage
	else:
		percentages = (float(state_total) / float(country_total)) * 100

	payload = {
		"state": state_query,
		"type": type_query,
		"start-date": start_date,
		"end-date": end_date,
		"std": std,
		"averages": averages,
		"percentages": percentages,
	}
	
	return payload


def is_in_queue(x, q):
   with q.mutex:
      return x in q.queue

def exists(self, item):
   if item in (x[1] for x in self.heap):
   	return True

def Only_Country_Analytic(country_query, state_query, type_query, start_date, end_date):
	from .urls import data_layer

	# passing in cities like chicago / LA, which doesnt have valid dates for 3/30/2021
	dates_dict = data_layer.countries_data.get(country_query).states.get(state_query).dates

	type_nums = Get_Date_Range(type_query, start_date, end_date, dates_dict)
	
	"""
		pq(max value, state)
		range is same for everyone variable for total days (type num len)
	"""
	if not exists(data_layer.only_country_analytic_pq, state_query):
		data_layer.only_country_analytic_pq.put((max(type_nums), state_query))

	

# Returns a list of the dates in between two ranges
def Get_Date_Range(type_query, start_date, end_date, dates_dict):
	type_nums = []

	# TODO: Handle dates that DNE
	# TODO: Handle same date
	if start_date == end_date:
		# print("IN GET DATE RANGE", dates_dict.get(start_date))
		type_nums.append(float(dates_dict.get(start_date).reprJSON()[type_query]))
		# print("START IS EQUAL TO END")
		return type_nums

	# TODO: write function that grabs all dates in between the start and end and returns a list

	# Get index of our start date and start iterating from there until we reach the end date
	# how about get a list of the keys(dates) we need to iterate over and plug them into our dict
	date_keys_list = list(dates_dict.keys())
	# slicing list of keys to get the date ranges in between included them
	for date_key in date_keys_list[
		date_keys_list.index(start_date) : date_keys_list.index(end_date)
	]:
		# TODO: maybe add a function that maps date object to a dict,
		# so we dont have to check each type case w/ a cn if
		# temp fix bc lazy, but it lets me not have to use a bunch of conditionals xd
		type_nums.append(
			float(dates_dict.get(date_key).reprJSON()[type_query])
		)  # credit to alan

	"""
	[0,2,3,4,...23423]
	"""
		
	# print(date_key)
	# print(test)
	return type_nums
