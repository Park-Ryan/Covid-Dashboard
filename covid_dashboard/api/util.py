import heapq
from os import stat

from .data_layer.load_csv import *
from array import array
import math
from queue import PriorityQueue
import time
from datetime import datetime
from datetime import timedelta

did_change = False


def Get_Top_5_Countries_Deaths():
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()
	country_deaths = 0.0
	payload = []
	tmp_list = []
	death_dict = {}
	state_max = 0.0
	empty = ""


	heapq.heapify(data_layer.top_5_death_heap)
	data_layer.top_5_death_heap.sort()

	for i in range(0, 5):
		payload.append(
			{
				"Country": data_layer.top_5_death_heap[i][1].country_name,
				"State": empty,
				"Date": empty,
				"Types": {
					"Confirmed": empty,
					"Deaths": data_layer.top_5_death_heap[i][1].total_deaths,
					"Recovered": empty,
				},
			}
		)
	return payload


def Get_Top_5_Countries_Confirmed():
	from .urls import data_layer

	payload = []
	empty = ""
	data_layer.top_5_confirmed_heap.sort()
	for i in range(0, 5):
		payload.append(
			{
				"Country": data_layer.top_5_confirmed_heap[i][1].country_name,
				"State": empty,
				"Date": empty,
				"Types": {
					"Confirmed": empty,
					"Deaths": data_layer.top_5_confirmed_heap[i][1].total_confirmed,
					"Recovered": empty,
				},
			}
		)
	return payload


def Update_Deaths(country_name, updated_value):
	from .urls import data_layer

	"""
	1. Get the PQ
	2. Search country in that PQ
	3. Replace/Update that country with specified value

	"""
	for index in range(0, len(data_layer.top_5_death_heap)):
		if country_name == data_layer.top_5_death_heap[index][1].country_name:
			tmp_total = float(data_layer.top_5_death_heap[index][1].total_deaths)
			data_layer.top_5_death_heap[index][1].total_deaths = abs(
				float(updated_value) - tmp_total
			)
			print(data_layer.top_5_death_heap[index][1].total_deaths)
	heapq.heapify(data_layer.top_5_death_heap)


def Update_Confirmed(country_name, updated_value):
	from .urls import data_layer

	"""
	1. Get the PQ
	2. Search country in that PQ
	3. Replace/Update that country with specified value

	"""
	for index in range(0, len(data_layer.top_5_confirmed_heap)):
		if country_name == data_layer.top_5_confirmed_heap[index][1].country_name:
			tmp_total = float(data_layer.top_5_confirmed_heap[index][1].total_confirmed)
			data_layer.top_5_confirmed_heap[index][1].total_confirmed = abs(
				float(updated_value) - tmp_total
			)
	heapq.heapify(data_layer.top_5_confirmed_heap)


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
	# print(payload)
	return payload


def Get_Top_5_States_Deaths():
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
	return payload


def Get_Top_5_States_Recovered():
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
	# print(payload)
	return payload

# Getter functions
def Find_Country(country):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	if country in tmp_countries_list:
		return 1
	else:
		return 0


def Find_State(country, state):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			return 1
		else:
			return 0
	else:
		return 0


def Find_Date(country, state, type, date):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			if date in tmp_countries_list[country].states[state].dates:
				return 1
			else:
				return 0
		else:
			return 0
	else:
		return 0


def Find_Cases(country, state, type, date):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			if date in tmp_countries_list[country].states[state].dates:
				if type == "Confirmed":
					return tmp_countries_list[country].states[state].dates[date].reprJSON()[type]
				elif type == "Deaths":
					return tmp_countries_list[country].states[state].dates[date].reprJSON()[type]
				elif type == "Recovered":
					return tmp_countries_list[country].states[state].dates[date].reprJSON()[type]
			else:
				return 0
		else:
			return 0
	else:
		return 0


# Backup CSV
def Backup_Csv(path):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

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


# Create(Country: USA, State: California, Confirmed : 0, Deaths: 0, Recovered: 0, Date: 9/11/2021)
def Create_Csv(country, state, type, date, amount):
	from .urls import data_layer

	countries_dict = data_layer.countries_data

	need_update = False

	# this checks if the country is in the country list dictionary
	# if country in tmp_countries_list:
	# date_obj is a date object that will be added to the country list
	# Since function only takes in specified input then we have to check
	# which type it is. After entering specified amount for type then
	# make the other 2 types default 0

	if country in countries_dict:
		if date in countries_dict[country].states[state].dates:
			#print("Create Exist. Go To Edit Instead.")
			print("")
		else:

			if type == "Deaths":
				date_obj = Date(date, "0", str(amount), "0")
				Update_Deaths(country, amount)
			elif type == "Confirmed":
				date_obj = Date(date, str(amount), "0", "0")
				Update_Confirmed(country, amount)
			elif type == "Recovered":
				# then make a date object to add to the country object
				date_obj = Date(date, "0", "0", str(amount))
				# sets country object dates to the date object
			date_obj.init_reprJSON()
			need_update = True
			countries_dict[country].states[state].dates[date] = date_obj

	else:
		country_obj = Country(country)
		country_obj.states[state] = State(state, country)
		if type == "Deaths":
			country_obj.total_deaths = float(amount)
			date_obj = Date(date, "0", str(amount), "0")
		elif type == "Confirmed":
			country_obj.total_confirmed = float(amount)
			date_obj = Date(date, str(amount), "0", "0")
		elif type == "Recovered":
			date_obj = Date(date, "0", "0", str(amount))

		country_obj.states[state].dates[date] = date_obj

		countries_dict[country] = country_obj
		country_obj.init_reprJSON()

		if type == "Deaths":
			heapq.heappush(data_layer.top_5_death_heap, (-country_obj.total_deaths, country_obj))
			heapq.heapify(data_layer.top_5_death_heap)
			print(data_layer.top_5_death_heap[0][1].total_deaths)
		elif type == "Confirmed":
			heapq.heappush(
				data_layer.top_5_confirmed_heap, (-country_obj.total_confirmed, country_obj)
			)
			heapq.heapify(data_layer.top_5_confirmed_heap)

	# case_dict = dict(sorted(case_dict.items(), key=lambda item: item[1], reverse=True))
	start_time = time.time()

	ordered_data = dict(
		sorted(
			countries_dict[country].states[state].dates.items(),
			key=lambda x: datetime.strptime(x[0], "%m/%d/%Y"),
		)
	)
	countries_dict[country].states[state].dates = ordered_data

	# THIS TAKES FOREVER
	# NEVER USE SET AND GET COUNTRIES
	# data_layer.set_countries(countries_dict)

	if need_update:
		#print("Reached need update")
		Update_Value(country, state, type, date, amount)
		need_update = False

	elapsed_time = time.time() - start_time
	print("Time elapsed for weird block is : " + str(elapsed_time) + " seconds")


# only update the confirmed, deaths, or recovered cases
def Update_Csv(country, state, type, date, value):
	from .urls import data_layer

	tmp_countries_list = data_layer.get_countries()

	# See confirmed if condition for comments

	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			if date in tmp_countries_list[country].states[state].dates:
				if type == "Deaths":
					tmp_recovered = (
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Recovered"]
					)
					tmp_confirmed = (
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Confirmed"]
					)
					date_obj = Date(
						date,
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Confirmed"],
						str(float(value)),
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Recovered"],
					)
					tmp_countries_list[country].states[state].dates[date] = date_obj

					tmp_countries_list[country].states[state].dates[date].confirmed = tmp_confirmed
					tmp_countries_list[country].states[state].dates[date].deaths = str(float(value))
					tmp_countries_list[country].states[state].dates[date].recovered = tmp_recovered

					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Confirmed"
					] = tmp_confirmed
					tmp_countries_list[country].states[state].dates[date].reprJSON()["Deaths"] = str(
						float(value)
					)
					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Recovered"
					] = tmp_recovered

					Update_Deaths(country, value)
					print("Edit Deaths")

				elif type == "Recovered":
					tmp_deaths = (
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Deaths"]
					)
					tmp_confirmed = (
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Confirmed"]
					)
					date_obj = Date(
						date,
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Confirmed"],
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Deaths"],
						str(float(value)),
					)
					tmp_countries_list[country].states[state].dates[date] = date_obj

					tmp_countries_list[country].states[state].dates[date].confirmed = tmp_confirmed
					tmp_countries_list[country].states[state].dates[date].deaths = tmp_deaths
					tmp_countries_list[country].states[state].dates[date].recovered = str(float(value))

					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Confirmed"
					] = tmp_confirmed
					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Deaths"
					] = tmp_deaths
					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Recovered"
					] = str(float(value))
					print("Edit Recovered")

				elif type == "Confirmed":
					tmp_deaths = (
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Deaths"]
					)
					tmp_recovered = (
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Recovered"]
					)
					date_obj = Date(
						date,
						str(float(value)),
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Deaths"],
						tmp_countries_list[country].states[state].dates[date].reprJSON()["Recovered"],
					)
					tmp_countries_list[country].states[state].dates[date] = date_obj

					tmp_countries_list[country].states[state].dates[date].confirmed = str(float(value))
					tmp_countries_list[country].states[state].dates[date].deaths = tmp_deaths
					tmp_countries_list[country].states[state].dates[date].recovered = tmp_recovered

					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Confirmed"
					] = str(float(value))
					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Deaths"
					] = tmp_deaths
					tmp_countries_list[country].states[state].dates[date].reprJSON()[
						"Recovered"
					] = tmp_recovered

					Update_Confirmed(country, value)
					print("Edit Confirmed")
				else:
					print("Edit doesnt work")
			else:
				print("Edit couldn't find date")

	Update_Value(country, state, type, date, value)
	data_layer.set_countries(tmp_countries_list)


# type doesn't matter because you're deleting the whole row of values
# i.e for 01/20/2020 you would delete the whole row
def Delete_Csv(country, state, date, type):
	from .urls import data_layer

	# this checks if the country is in the country list dictionary
	# for key in tmp_countries_list:
	if country in data_layer.countries_data:
		if state in data_layer.countries_data[country].states:
			if date in data_layer.countries_data[country].states[state].dates:
				Delete_Value(country, state, type, date)

		else:
			print("State no exist")
	else:
		print("Doesn't exist")


def Delete_Value(country, state, type, date):
	from .urls import data_layer

	"""
		Need the previous value to compute the daily value to subtract from next values
		Grab the key list from .keys()
		Grab the value list from .values()
		Iterate through key_list until date == key_list[i]
		
		Get the value_list[i] and value_list[i-1]
		This will get the daily value
		Store into a variable to subtract 
		Then for loop through values from that given that
	
	"""

	flag = False

	key_list = list(data_layer.countries_data[country].states[state].dates.keys())
	value_list = list(
		data_layer.countries_data[country].states[state].dates.values()
	)  # dict_values([...])
	# [date_obj1, ... , n-1]

	# TODO what if deleting first date and last date?
	# if first date, subtract its value from every future date and delete at end
	# if last date, delete it
	subtract_amount = 0
	i = key_list.index(date)
	if i == 0:
		if type == "Confirmed":
			subtract_amount = float(value_list[0].confirmed)
			Update_Confirmed(country, subtract_amount)
		if type == "Deaths":
			print("Values list index of 0: ")
			print(value_list[0].deaths)
			subtract_amount = float(value_list[0].deaths)
			Update_Deaths(country, subtract_amount)
		if type == "Recovered":
			subtract_amount = float(value_list[0].recovered)

	elif i == len(key_list):
		del data_layer.countries_data[country].states[state].dates[date]
		return
	else:
		if type == "Confirmed":
			subtract_amount = float(value_list[i].confirmed) - float(value_list[i - 1].confirmed)
			Update_Confirmed(country, subtract_amount)
		if type == "Deaths":
			subtract_amount = float(value_list[i].deaths) - float(value_list[i - 1].deaths)
			Update_Deaths(country, subtract_amount)
		if type == "Recovered":
			subtract_amount = float(value_list[i].recovered) - float(value_list[i - 1].recovered)

	for date_key, date_val in (
		data_layer.countries_data[country].states[state].dates.items()
	):
		if flag:
			if type == "Confirmed":
				tmp_amount = float(date_val.confirmed)
				tmp_amount -= subtract_amount
				date_val.confirmed = str(tmp_amount)
			if type == "Deaths":
				tmp_amount = float(date_val.deaths)
				tmp_amount -= subtract_amount
				date_val.deaths = str(tmp_amount)
			if type == "Recovered":
				tmp_amount = float(date_val.recovered)
				tmp_amount -= subtract_amount
				date_val.recovered = str(tmp_amount)
			data_layer.countries_data[country].states[state].dates[date_key].init_reprJSON()
		if date_key == date:
			flag = True

	del data_layer.countries_data[country].states[state].dates[date]
	# updating the countries dict


def Update_Value(country, state, type, date, amount):
	from .urls import data_layer

	# updating the countries dict
	dates_dict = data_layer.countries_data.get(country).states.get(state).dates
	date_keys_list = list(dates_dict.keys())
	for date_key in date_keys_list[date_keys_list.index(date) :]:
		if date_key != date:
			tmp_amount = float(dates_dict[date_key].reprJSON()[type]) + float(amount)
			if type == "Confirmed":
				dates_dict[date_key].confirmed = str(tmp_amount)
			elif type == "Deaths":
				dates_dict[date_key].deaths = str(tmp_amount)
			elif type == "Recovered":
				dates_dict[date_key].recovered = str(tmp_amount)
			dates_dict[date_key].init_reprJSON()

	data_layer.countries_data[country].states[state].dates = dates_dict


def Get_Filtered_Data(countryFilter, stateFilter, typeFilter, dateFilter):

	# putting payload into array so we can iterate thru and put into table?
	# list of jsons/dicts
	payload = []

	# importing the data layer object so we can use the functions within the method
	from .urls import data_layer

	countries_list = data_layer.countries_data
	# print("DATA LAYER: ", countries_list[countryFilter].states[stateFilter].dates.items())
	# countries_list[countryFilter].states[stateFilter].dates.items()
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

	# add this temporay condition to avoid error when adding a ENTIRELY new country i.e. Hololive
	if countryFilter in countries_list:
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

	# if payload is empty, no results found / api responsed with nothing

	return payload


# TODO: if state is empty, calc the analytics for country
# if type is empty, calc all the anayltics for each type
# if
def Get_Analytics(country_query, state_query, type_query, start_date, end_date) -> dict:
	from .urls import data_layer

	# passing in cities like chicago / LA, which doesnt have valid dates for 3/30/2021
	dates_dict = data_layer.countries_data.get(country_query).states.get(state_query).dates

	# function to get the date range
	type_nums = Get_Date_Range(
		country_query, state_query, type_query, start_date, end_date, dates_dict
	)
	# print("TYPE_NUMS: ", type_nums)
	averages = max(type_nums) / len(type_nums)
	variance = sum(pow(x - averages, 2) for x in type_nums)
	variance /= len(type_nums)
	std = math.sqrt(variance)

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

	type_nums = Get_Date_Range(country_query, type_query, start_date, end_date, dates_dict)

	"""
		pq(max value, state)
		range is same for everyone variable for total days (type num len)
	"""
	if not exists(data_layer.only_country_analytic_pq, state_query):
		data_layer.only_country_analytic_pq.put((max(type_nums), state_query))


# Returns a list of the dates in between two ranges
def Get_Date_Range(
	country_query, state_query, type_query, start_date, end_date, dates_dict
):
	from .urls import data_layer

	countries_list = data_layer.get_countries()

	type_nums = []
	# TODO: Handle dates that DNE
	# TODO: Handle same date

	# TODO: write function that grabs all dates in between the start and end and returns a list

	"""
	USER inputs nothing
	purpose of our analytic is to calculate across the entire time. Start of covid 

	if there's a date then we do the last seven days 
	
	
	"""
	tmp_start_date = end_date

	array_dates = []
	int_date = datetime.strptime(tmp_start_date, "%m/%d/%Y")

	if start_date or end_date == "":
		for x in range(0, len(dates_dict)):
			start_int_date = int_date.strftime("%m/%d/%Y")
			array_dates.insert(0, start_int_date)
			int_date -= timedelta(days=1)

		for x in range(0, len(dates_dict)):
			if array_dates[x] in countries_list[country_query].states[state_query].dates:
				type_nums.append(float(dates_dict.get(array_dates[x]).reprJSON()[type_query]))
		return type_nums
	else:
		for x in range(8):
			start_int_date = int_date.strftime("%m/%d/%Y")
			array_dates.insert(0, start_int_date)
			int_date -= timedelta(days=1)

		for x in range(7):
			if array_dates[x] in countries_list[country_query].states[state_query].dates:
				type_nums.append(float(dates_dict.get(array_dates[x]).reprJSON()[type_query]))

	return type_nums
