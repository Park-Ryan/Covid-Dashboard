#from .data_layer.load_csv import *

def Reverse_String(dict):

    payload = dict['payload_bus']

    payload = str(payload[::-1])

    payload = payload.replace("'",'"')

    return payload


def Get_Filtered_Data(countryFilter,stateFilter,typeFilter,dateFilter):

    filteredArray = []
    from .urls import data_layer
    countries_list = data_layer.get_countries()

    #countries_list[countryFilter].states[stateFilter].dates[dateFilter]
    if countryFilter != '' and dateFilter != '' and stateFilter != '':
        for val in countries_list.values():
            if val.country_name == countryFilter:            
                if dateFilter in countries_list[countryFilter].states[stateFilter].dates:
                    if typeFilter == '':        
                        
                        return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON())           
                        #print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Confirmed'])
                        #print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Recovered'])
                        #print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Deaths'])
                        
                    else:       
                        print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])
                        return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])
                    
                else:
                    print('no work') 
    #countries_list[countryFilter].states[stateFilter].dates[]
    elif countryFilter != '' and stateFilter != '' and dateFilter == '':
        for new_Date in countries_list[countryFilter].states[stateFilter].dates:
                if typeFilter == '':         
                        #return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON())           
                        print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Confirmed'])
                        #print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Recovered'])
                        #print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Deaths'])
                        
                else:    
                        print(countries_list[countryFilter].states[stateFilter].dates[new_Date].reprJSON()[typeFilter])
                        #return(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])
            #else:
                #print('countries_list[countryFilter].states[stateFilter].dates[] no work') 
                    
    #countries_list[countryFilter].states[].dates[]
    # for this case return json of all states(which includes dates) for that country
    elif countryFilter != '' and stateFilter == '' and dateFilter == '':
        array_of_types = []
        for valState in countries_list[countryFilter].states.values():
            for valDate in valState.dates:
                if valDate in valState.dates:
                    #since this checks all the date in the entire country
                    #have to add the json into an array before returning
                    if typeFilter == '':   
                        return(valState.dates[valDate].reprJSON())                
                        #print(valState.dates[valDate].reprJSON()['Confirmed'])
                        #print(valState.dates[valDate].reprJSON()['Recovered'])
                        #print(valState.dates[valDate].reprJSON()['Deaths'])
                        
                    else:
                        print(valState.dates[valDate].reprJSON()[typeFilter])      
                        #return(valState.dates[valDate].reprJSON()[typeFilter])
                        #array_of_types.append
                else:
                    print('countries_list[countryFilter].states[].dates[] no work')
    
    #countries_list[countryFilter].states[].dates[dateFilter]
    elif countryFilter != '' and stateFilter == '' and dateFilter != '': 
        for state in countries_list[countryFilter].states.values():
            if dateFilter in state.dates:
                if typeFilter == '':                   
                    return(state.dates[dateFilter].reprJSON()) # returns {date(key) : "01/22/2020" , "232132", ...}
                    
                else:
                    print(state.dates[dateFilter].reprJSON()[typeFilter])       
                    #return(state.dates[dateFilter].reprJSON()[typeFilter])
            #else:
                #print('countries_list[countryFilter].states[].dates[dateFilter] no work')

    #countries_list[].states[].dates[dateFilter]
    elif countryFilter == '' and stateFilter == '' and dateFilter != '': 
        for valCountry in countries_list.values():
            for valState in valCountry.states.values():
                if dateFilter in valState.dates: 
                    if typeFilter == '':    
                        # dont need to return json bc we are only printing to console   
                        return(valState.dates[dateFilter].reprJSON())
                        # convert later when sending response to frontend eg. .reprJSON()
                        # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Confirmed'])
                        # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Recovered'])
                        # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Deaths'])                    
                    else:
                        print(valState.dates[dateFilter].reprJSON()[typeFilter])
                        #return(valState.dates[dateFilter].reprJSON())
                #else:
                    #print('countries_list[].states[].dates[dateFilter] no work')

    #countries_list[].states[stateFilter].dates[dateFilter]
    elif countryFilter == '' and stateFilter != '' and dateFilter != '':
        for valCountry in countries_list.values():
            for state_val in valCountry.states.values():
                if state_val.state_name == stateFilter:
                    if dateFilter in state_val.dates: #special
                        if typeFilter == '':    
                            # dont need to return json bc we are only printing to console   
                            return(state_val.dates[dateFilter].reprJSON())
                            # convert later when sending response to frontend eg. .reprJSON()
                            # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Confirmed'])
                            # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Recovered'])
                            # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Deaths'])                    
                        else:
                            print(state_val.dates[dateFilter].reprJSON()[typeFilter])


    #countries_list[].states[stateFilter].dates[]
    elif countryFilter == '' and stateFilter != '' and dateFilter == '':
        for valCountry in countries_list.values():
            for valState in valCountry.states.values():
                if valState.state_name == stateFilter:
                    #print(valState.state_name)
                    for valDate in valState.dates:
                        if valDate in valState.dates:
                            if typeFilter == '':    
                                # dont need to return json bc we are only printing to console   
                                return(valState.dates[dateFilter].reprJSON())
                                # convert later when sending response to frontend eg. .reprJSON()
                                # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Confirmed'])
                                # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Recovered'])
                                # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Deaths'])                    
                            else:
                                print(valState.dates[valDate].reprJSON()[typeFilter])

#countries_list[countryFilter].states[stateFilter].dates[dateFilter]
#countries_list[countryFilter].states[stateFilter].dates[]
#countries_list[countryFilter].states[].dates[]

#countries_list[countryFilter].states[].dates[dateFilter]

#countries_list[].states[stateFilter].dates[]
#countries_list[].states[stateFilter].dates[dateFilter]

#countries_list[].states[].dates[dateFilter]



