#from .data_layer.load_csv import *

def Reverse_String(dict):

    payload = dict['payload_bus']

    payload = str(payload[::-1])

    payload = payload.replace("'",'"')

    return payload


def Get_Filtered_Data(countryFilter,stateFilter,typeFilter,dateFilter):

    filteredArray = []
    #data_layer = DataLayer()
    #data_layer.initLoadCSV("api/data/archive/covid_19_data.csv")
    # tempData = DataLayer()
    # tempData.initLoadCSV("api/data/archive/covid_19_data.csv")
    from .urls import data_layer
    countries_list = data_layer.get_countries()

    if countryFilter != '' and dateFilter != '' and stateFilter != '':
        for val in countries_list.values():
            if val.country_name == countryFilter:            
                if dateFilter in countries_list[countryFilter].states[stateFilter].dates:

                    #the print should be return, typefiler should return( .. + .. + ..) fix later
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

    elif countryFilter != '' and stateFilter == '' and dateFilter == '':
        for valState in countries_list[countryFilter].states.values():
            for valDate in valState.dates:
                if valDate in valState.dates:
                    if typeFilter == '':   
                        return(valState.dates[valDate].reprJSON())                
                        #print(valState.dates[valDate].reprJSON()['Confirmed'])
                        #print(valState.dates[valDate].reprJSON()['Recovered'])
                        #print(valState.dates[valDate].reprJSON()['Deaths'])
                        
                    else:
                        #print(valState.dates[valDate])      
                        return(valState.dates[valDate].reprJSON()[typeFilter])
    
    elif countryFilter != '' and dateFilter != '' and stateFilter == '': 
        for state in countries_list[countryFilter].states.values():
            #if dateFilter in countries_list[countryFilter].states[state].dates:
            if dateFilter in state.dates:
                if typeFilter == '':                   
                    return(state.dates[dateFilter].reprJSON()) # returns {date(key) : "01/22/2020" , "232132", ...}
                    
                else:       
                    return(state.dates[dateFilter].reprJSON()[typeFilter])

    elif countryFilter == '' and stateFilter == '' and dateFilter != '':
        #no state, no date
        #if country has state then date, state
        #if country but no state then just date
        #country => state => date
        #countr => date
            #if val.country_name == countryFilter:  
        #print("hello")
        for valCountry in countries_list.values():
            #print(countries_list[valCountry].dates[dateFilter].reprJSON()[typeFilter])
            for valState in valCountry.states.values():
                #if dateFilter in countries_list[valCountry].states[valState].dates: #special
                if dateFilter in valState.dates: #special
                    if typeFilter == '':    
                        # dont need to return json bc we are only printing to console   
                        return(valState.dates[dateFilter].reprJSON())
                        # convert later when sending response to frontend eg. .reprJSON()
                        # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Confirmed'])
                        # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Recovered'])
                        # print(countries_list[valCountry].states[valState].dates[dateFilter].reprJSON()['Deaths'])                    
                    else:
                        return(valState.dates[dateFilter].reprJSON())
                    