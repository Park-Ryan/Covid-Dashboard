# import "RyansData" from "../../"

def Reverse_String(dict):

    payload = dict['payload_bus']

    payload = str(payload[::-1])

    payload = payload.replace("'",'"')

    return payload


# def Get_Filtered_Data(countryFilter,stateFilter,typeFilter,dateFilter):


#     filteredArray = []

#     for countryKey, countryVal in ryansDictionary:
#         if countryKey is countryFilter:
#             filteredArray.append(countryVal)
    
#     #RETURNS A LIST OF JSON of filtered data
#     pass