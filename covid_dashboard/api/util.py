from os import stat
from .data_layer.load_csv import *
import json
import copy

def Reverse_String(dict):

	payload = dict["payload_bus"]

	payload = str(payload[::-1])

	payload = payload.replace("'", '"')

	return payload




#def Copy_Csv(self, pathOfOriginal):
	
#Backup CSV
def Backup_Csv(path):
	from .urls import data_layer
	tmp_countries_list = data_layer.get_countries()

	
		#print(tmp_countries_list["US"])

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
					tmp_join = [SNo,date, csv_state,csv_country, date, confirmed, deaths, recovered]
					tmp_string = ",".join(tmp_join)
					tmp_string += "\n"
					outfile.write(tmp_string)



# SNo,ObservationDate,Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered
#Create(Country: USA, State: California, Confirmed : 0, Deaths: 0, Recovered: 0, Date: 9/11/2021)
def Create_Csv(country, state, type, date, value):
	from .urls import data_layer
	tmp_countries_list = data_layer.get_countries()
	
	#1. user wants to add a country 
	#2. user wants to add a state
	#3. user wants to add a date
	
	if country not in tmp_countries_list.keys():
		country_obj = Country(country)
		state_obj = State(state, country)
		country_obj.states[state] = state_obj
		if type == "Deaths":
					date_obj = Date( 
									date, 
									"", 
									str(value), 
									""
									) 
					country_obj.states.get(state).dates[date] = date_obj
					tmp_countries_list[country] = country_obj
		elif type == "Recovered":
					date_obj = Date( 
									date, 
									"",
									"",
									str(value)
									) 
					country_obj.states.get(state).dates[date] = date_obj
					tmp_countries_list[country] = country_obj
		elif type == "Confirmed":			
					date_obj = Date( 
									date, 
									str(value), 
									"", 
									""
									) 
					country_obj.states.get(state).dates[date] = date_obj
					tmp_countries_list[country] = country_obj
	data_layer.set_countries(tmp_countries_list)
					



	

	

#only update the confirmed, deaths, or recovered cases
def Update_Csv(country, state, type, date, value):
	from .urls import data_layer
	tmp_countries_list = data_layer.get_countries()
	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			if date in tmp_countries_list[country].states[state].dates:
				if type == "Deaths":
					#print(tmp_countries_list[country].states[state].dates[date].reprJSON()[type])
					date_obj = Date( 
									date, 
									tmp_countries_list[country].states[state].dates[date].confirmed, 
									str(value), 
									tmp_countries_list[country].states[state].dates[date].recovered
									) 
					tmp_countries_list[country].states[state].dates[date] = date_obj
					print("Edit Deaths")
					#print(tmp_countries_list[country].states[state].dates[date].reprJSON()[type])
				elif type == "Recovered":
					date_obj = Date( 
									date, 
									tmp_countries_list[country].states[state].dates[date].confirmed, 
									tmp_countries_list[country].states[state].dates[date].deaths,
									str(value)
									) 
					tmp_countries_list[country].states[state].dates[date] = date_obj
					print("Edit Recovered")
				elif type == "Confirmed":			
					date_obj = Date( 
									date, 
									str(value), 
									tmp_countries_list[country].states[state].dates[date].deaths, 
									tmp_countries_list[country].states[state].dates[date].recovered
									) 
					tmp_countries_list[country].states[state].dates[date] = date_obj
					print("Edit Confirmed")
				else:
					print("Update doesnt work")
			else:
				print("Update couldn't find date")
	
	print(tmp_countries_list.get(country).states.get(state).dates.get(date).reprJSON())
	data_layer.set_countries(tmp_countries_list)

#type doesn't matter because you're deleting the whole row of values 
#i.e for 01/20/2020 you would delete the whole row
def Delete_Csv(country, state, date):
	from .urls import data_layer
	tmp_countries_list = data_layer.get_countries()

	#this checks if the country is in the country list dictionary
	#for key in tmp_countries_list:
	if country in tmp_countries_list:
		if state in tmp_countries_list[country].states:
			if date in tmp_countries_list[country].states[state].dates:
				#print(tmp_countries_list[country].states[state].dates[date])
				del tmp_countries_list[country].states[state].dates[date]
				#print(tmp_countries_list[country].states[state].dates[date])
				#print(tmp_countries_list)
		else:
			print("State no exist")
	else:
		print("Doesn't exist")

	data_layer.set_countries(tmp_countries_list)

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
