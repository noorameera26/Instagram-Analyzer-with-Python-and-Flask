import requests
import json

"""
This function store things like access token, client ID, client secret (anything that we won't globally define)
"""

def getCreds():
    creds = dict()
    creds['access_token'] = 'EAARIUQ29Ba4BALEoYJODJZBN4N44BoOLPZCmT1ZC0A4kQlZCqQWTGwnlyyDKhW1Qnnhfrih9kI8gZABZAZCCyYRof0AFthVZAFKZAHxHqV4p2M4wKs71fnNvwTgaMAXbltTNPJbfKQeagRMU9lhEJ3UTZBztocGSXkTwGtOcwy8noNFQNAHK2FaLC91urmiiTUOSY9B5b5HXIHzQZDZD'
    creds['client_id'] = '1205412866885038'
    creds['client_secret'] = '9b0e82d2e09247fbf3bd3c8f253b33cc'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v14.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'

    return creds

"""
This function make a get request to any instagrap graph API that we specify
"""
def makeApiCall(url, endpointParams, debug = 'no'):
    data = requests.get(url, endpointParams)
    
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent = 4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent = 4)

    if(debug == 'yes'):
        displayApiCallData(response)

    return response

"""
This function display API call data
"""
def displayApiCallData(response):
    print("\n URL:")
    print(response['url'])
    print("\n Endpoint Params:")
    print(response['endpoint_params_pretty'])
    print("\n Response:")
    print(response['json_data_pretty'])
