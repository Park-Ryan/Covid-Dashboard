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
    #print(countries_list)

    if countryFilter != '' and dateFilter != '' and stateFilter != '':
        for val in countries_list.values():
            if val.country_name == countryFilter:            
                if dateFilter in countries_list[countryFilter].states[stateFilter].dates:

                    #the print should be return, typefiler should return( .. + .. + ..) fix later
                    if typeFilter == '':                   
                        print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Confirmed'])
                        print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Recovered'])
                        print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()['Deaths'])
                        
                    else:       
                        print(countries_list[countryFilter].states[stateFilter].dates[dateFilter].reprJSON()[typeFilter])
                    
                else:
                    print('no work') 

    # elif countryFilter != '' and stateFilter == '' and dateFilter == '':
    #     #print('work')
    #     stateArray = countries_list[countryFilter].states.values()
    #     #dateArray = countries_list
    #     print(stateArray)
        # for valState in stateArray:
        #     for valDate in countries_list[countryFilter].states[valState].dates:
        #         if valDate in countries_list[countryFilter].states[valState].dates:
        #             if typeFilter == '':                   
        #                 print(countries_list[countryFilter].states[valState].dates[valDate].reprJSON()['Confirmed'])
        #                 print(countries_list[countryFilter].states[valState].dates[valDate].reprJSON()['Recovered'])
        #                 print(countries_list[countryFilter].states[valState].dates[valDate].reprJSON()['Deaths'])
                        
        #             else:       
        #                 print(countries_list[countryFilter].states[valState].dates[valDate].reprJSON()[typeFilter])
    
    # elif countryFilter != '' and dateFilter != '' and stateFilter == '':
    #     #countries_list[countryFilter].states[].date[dateFilter]
    #     # for val in countries_list.values():
    #     #     if val.country_name == countryFilter:
    #     state_list =   
    #     for val in countries_list[countryFilter].states.values():
    #         if dateFilter in countries_list[countryFilter].states[val].dates:
    #             if typeFilter == '':                   
    #                 print(countries_list[countryFilter].states[val].dates[dateFilter].reprJSON()['Confirmed'])
    #                 print(countries_list[countryFilter].states[val].dates[dateFilter].reprJSON()['Recovered'])
    #                 print(countries_list[countryFilter].states[val].dates[dateFilter].reprJSON()['Deaths'])
                    
    #             else:       
    #                 print(countries_list[countryFilter].states[val].dates[dateFilter].reprJSON()[typeFilter])

    # elif countryFilter != '' and stateFilter != '': #dateFilter == ''
    #     #for val in countries_list.values():
    #     #for val in countries_list.values():
    #         #if val.country_name == countryFilter:            
    #             for valDate in countries_list[countryFilter].states[stateFilter].dates:
    #                 if valDate in countries_list[countryFilter].states[stateFilter].dates:
    #                     if typeFilter == '':                   
    #                         print(countries_list[countryFilter].states[stateFilter].dates[valDate].reprJSON()['Confirmed'])
    #                         print(countries_list[countryFilter].states[stateFilter].dates[valDate].reprJSON()['Recovered'])
    #                         print(countries_list[countryFilter].states[stateFilter].dates[valDate].reprJSON()['Deaths'])
                            
    #                     else:       
    #                         print(countries_list[countryFilter].states[stateFilter].dates[valDate].reprJSON()[typeFilter])

    # elif dateFilter != '': #countryFilter == '' and stateFilter == ''
    # #countries_list[].states[].date[dateFilter]
    #     for valCountry in countries_list.values():
    #         for valState in countries_list[valCountry].state.values():
    #             if dateFilter in countries_list[countryFilter].states[valState].dates:
    #                 if typeFilter == '':                   
    #                     print(countries_list[countryFilter].states[valState].dates[dateFilter].reprJSON()['Confirmed'])
    #                     print(countries_list[countryFilter].states[valState].dates[dateFilter].reprJSON()['Recovered'])
    #                     print(countries_list[countryFilter].states[valState].dates[dateFilter].reprJSON()['Deaths'])
                        
    #                 else:       
    #                     print(countries_list[countryFilter].states[valState].dates[dateFilter].reprJSON()[typeFilter])


    # #list of things
    # #countries_list[countryFilter].states[stateFilter].date[dateFilter] X
    # #countries_list[countryFilter].states[stateFilter].date[] X
    # #countries_list[countryFilter].states[].date[dateFilter] X
    # #countries_list[countryFilter].states[].date[]

    # #countries_list[].states[stateFilter].date[dateFilter]
    # #countries_list[].states[stateFilter].date[]

    # #countries_list[].states[].date[dateFilter] X

    # elif stateFilter != '':  
    #     for val in countries_list.states.values():
    #        if val.state_name == stateFilter:            
    #             print(dateFilter)
    #             if dateFilter in countries_list[countryFilter].states[stateFilter].dates:
    #                print(countries_list[countryFilter].states[stateFilter].dates[dateFilter])
    #             else:
    #                print('no work') 

#    if typeFilter is not None:
#        for typeVal in filteredArray:
#            if typeVal != typeFilter:
#                filteredArray.pop()

#    if dateFilter is not None:
#        for dateVal in filteredArray:
#            if dateVal != dateFilter:
#                filteredArray.pop()

#    print(newarray)
#     #RETURNS A LIST OF JSON of filtered data
#     pass