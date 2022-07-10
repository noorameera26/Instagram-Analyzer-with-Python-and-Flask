import requests
import json

"""
This function stores things like access token, client ID, client secret (anything that we won't globally define)
"""

def getCreds():
    creds = dict() #dictionary to store data
    creds['access_token'] = 'EAAIEmN8d1x0BALu7rCVA5O1rZAMZA88tIgO6RppZAynidZAeqWXB0kZCzb5bMUmMv91EyPvBRxtZBP8u2uwVZA2daraLvcOU6XaXg4PbGvkqJ2pypGp2jBJf9HBe9ZCBzZAqjqkUd3Lg2gXyE4H3m8hIpIA3rh91TqNCEB1cFhQaIKtGLIqTYdZBLnZBvZCk87oGZCUYWbHdQpEKSxAZDZD'
    #creds['access_token'] = 'EAAIEmN8d1x0BAOFinjHV2c681MUcGgBOD10Vr0qxzQkDecqGtzucZBT90J4DZCBJfEpxBO37b8ybpB9pyAHIFHyczJtuQzNG5GaBARCUYMR1wMODbu4HI7MlWPzHU8Am9MqAB9bP7QWZCi89Uehb1TKJqsOd7asYikHt8wtsImYMZB1A6BdyVZA1auPXsRMx6SApvOZBrMDgZDZD'
    creds['client_id'] = '568004578236189' #client user id 
    creds['client_secret'] = 'cf0e61ce2d0f62684062a60d94903c1b' #client secret id
    creds['graph_domain'] = 'https://graph.facebook.com/' #base domain name for api call
    creds['graph_version'] = 'v14.0' #API version
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no' #debug mode for api call -> call displayApiCallData() method
    creds['page_id'] = '100273202761597'
    creds['instagram_account_id'] = '17841454060525215' #ig user id
    creds['ig_username'] = 'noorameera26' #ig username

    return creds

"""
This function makes a get request to any instagrap graph API that we specify
"""
def makeApiCall(url, endpointParams, debug = 'no'):
    data = requests.get(url, endpointParams)
    
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['json_data'] = json.loads(data.content)
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent = 4)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent = 4)

    if(debug == 'yes'):
        displayApiCallData(response)

    return response

"""
This function displays API call data
"""
def displayApiCallData(response):
    print("\n URL:")
    print(response['url'])
    print("\n Endpoint Params:")
    print(response['endpoint_params_pretty'])
    print("\n Response:")
    print(response['json_data_pretty'])
