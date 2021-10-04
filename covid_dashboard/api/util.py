def Reverse_String(dict):

    payload = dict['payload_bus']

    payload = str(payload[::-1])

    payload = payload.replace("'",'"')

    return payload