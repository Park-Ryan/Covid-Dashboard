#from .data_layer.load_csv import *

def Reverse_String(dict):

    payload = dict['payload_bus']

    payload = str(payload[::-1])

    payload = payload.replace("'",'"')

    return payload


def Get_Filtered_Data(countryFilter,stateFilter,typeFilter,dateFilter):

    filteredArray = {}
    from .urls import data_layer
    countries_list = data_layer.get_countries()

    #countries_list[countryFilter].states[stateFilter].dates[dateFilter]
    if countryFilter != '' and dateFilter != '' and stateFilter != '':
        for key, val in countries_list.items():
            if val.country_name == countryFilter:            
                if dateFilter in countries_list[countryFilter].states[stateFilter].dates:
                    if typeFilter == '':        
                        #return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON())           
                        filteredArray[key]=(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON())
                        
                    else:       
                        #print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])
                        filteredArray[key] = countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter]
                        #filteredArray.append(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])

                        #return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])
                    
                else:
                    print('no work') 
    #countries_list[countryFilter].states[stateFilter].dates[]
    elif countryFilter != '' and stateFilter != '' and dateFilter == '':
        
        for key, new_Date in countries_list[countryFilter].states[stateFilter].dates.items():
                if typeFilter == '':         
                        #return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON())           
                        filteredArray[key] = new_Date.reprJSON()
                        
                else:    
                        #print(countries_list[countryFilter].states[stateFilter].dates[new_Date].reprJSON()[typeFilter])
                        filteredArray[key] = new_Date.reprJSON()[typeFilter]
                        #filteredArray[key] = (countries_list[countryFilter].states[stateFilter].dates[new_Date].reprJSON()[typeFilter])
                        #return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])
            #else:
                #print('countries_list[countryFilter].states[stateFilter].dates[] no work') 
                    
    #countries_list[countryFilter].states[].dates[]
    # for this case return json of all states(which includes dates) for that country
    elif countryFilter != '' and stateFilter == '' and dateFilter == '':
        print('here')
        for valState in countries_list[countryFilter].states.values(): 
            for date, valDate in valState.dates.items(): 
                if date in valState.dates: 
                    #print('something') #stil  this prints nothing
                    #print(valState.dates)
                    if typeFilter == '':   
                        #return(valState.dates[valDate].reprJSON())                
                        filteredArray[date] = valDate.reprJSON()
                        
                    else:
                        #print(valState.dates[valDate].reprJSON()[typeFilter])
                        filteredArray[date] = valDate.reprJSON()
                        #return(valState.dates[valDate].reprJSON()[typeFilter])
                #else: the code goes here saying that it fail the if condition 
                    #print('countries_list[countryFilter].states[].dates[] no work')
                    
    

    #countries_list[countryFilter].states[].dates[dateFilter]
    elif countryFilter != '' and stateFilter == '' and dateFilter != '': 
        for key, state in countries_list[countryFilter].states.items(): #'dict' object has no attribute 'item' pretty sure it's items
            if dateFilter in state.dates:
                if typeFilter == '':                   
                    #return(state.dates[dateFilter].reprJSON()) # returns {date(key) : "01/22/2020" , "232132", ...}
                    filteredArray[key] = state.reprJSON()

                else:
                    #print(state.dates[dateFilter].reprJSON()[typeFilter])
                    #filteredArray.append(state.dates[dateFilter].reprJSON()[typeFilter])   
                    #return(state.dates[dateFilter].reprJSON()[typeFilter])
                    filteredArray[key] = state.dates[dateFilter].reprJSON()[typeFilter]
                    
            #else:
                #print('countries_list[countryFilter].states[].dates[dateFilter] no work')

    #countries_list[].states[].dates[dateFilter]
    elif countryFilter == '' and stateFilter == '' and dateFilter != '': 
        for valCountry in countries_list.values():
            for key, valState in valCountry.states.items():
                if dateFilter in valState.dates: 
                    if typeFilter == '':    
                        #return(valState.dates[dateFilter].reprJSON())
                        filteredArray[key] = valState.dates[dateFilter].reprJSON()
                    else:
                        #print(valState.dates[dateFilter].reprJSON()[typeFilter])
                        filteredArray[key] = valState.dates[dateFilter].reprJSON()[typeFilter]
                        #return(valState.dates[dateFilter].reprJSON())
                #else:
                    #print('countries_list[].states[].dates[dateFilter] no work')

    #countries_list[].states[stateFilter].dates[dateFilter]
    elif countryFilter == '' and stateFilter != '' and dateFilter != '':
        for valCountry in countries_list.values():
            for key, state_val in valCountry.states.items():
                if state_val.state_name == stateFilter:
                    if dateFilter in state_val.dates: #special
                        if typeFilter == '':    
                            filteredArray[key] = (state_val.dates[dateFilter].reprJSON())                  
                        else:
                            #print(state_val.dates[dateFilter].reprJSON()[typeFilter])
                            filteredArray[key] = (state_val.dates[dateFilter].reprJSON()[typeFilter])


    #countries_list[].states[stateFilter].dates[]
    elif countryFilter == '' and stateFilter != '' and dateFilter == '':
        for valCountry in countries_list.values():
            if stateFilter in valCountry.states:
                for key, valDate in valCountry.states[stateFilter].dates.items():
                    if key in valCountry.states[stateFilter].dates:
                        if typeFilter == '':    
                            filteredArray[key] = (valDate.reprJSON())                    
                        else:
                            #print(valState.dates[valDate].reprJSON()[typeFilter])
                            filteredArray[key] = (valDate.reprJSON()[typeFilter])
                            
    #print(filteredArray)
    return filteredArray

#countries_list[countryFilter].states[stateFilter].dates[dateFilter]
#countries_list[countryFilter].states[stateFilter].dates[]
#countries_list[countryFilter].states[].dates[]

#countries_list[countryFilter].states[].dates[dateFilter]

#countries_list[].states[stateFilter].dates[]
#countries_list[].states[stateFilter].dates[dateFilter]

#countries_list[].states[].dates[dateFilter]



