import requests
import json

"""
This function stores things like access token, client ID, client secret (anything that we won't globally define)
"""
def getCreds():
    creds = dict() #dictionary to store data
    #short lived token:
    #creds['access_token'] = 'EAAIEmN8d1x0BAI8enjb3z6oGoksvUKAbgnAlLBhwsQNlcCmiWDn4OLW4gZCEYfjBsL73zQsPgmuklL2lGTOXezAGufmncSfZBI3pXRlFsSG09nhkq8oUSL6bc2tDZBhMCcZAPbb6kv0IzlAsPztWV819K8ENyw5r1kqMxYW2hMzE0M9sn72g4YxJSe0Mcu6ZBzvIweRjjYNi9AiMCnbXE'
    #long lived lived token:
    creds['access_token'] = 'EAAIEmN8d1x0BABLUk9ZC1yoKfM7gaSjgLBtERrwTZCzyFGC7ZA8A7hH27zDcv3tqbtkbjHhzRKas9zYPUK792z60OSa1JQSZA5hpBZADHtQrcygQsQOn24w5ddm5v6bwkWiA09ISIcefW92inSYsl6xCej8oQe1bPLpdGOgkutbUPCqMYqWUb'
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
This function makes a get request to any instagram graph API that we specify
"""
def makeApiCall(url, endpointParams, debug = 'no'):
    data = requests.get(url, endpointParams) 
    
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['json_data'] = json.loads(data.content) #loads() parses the JSON string into a Python dictionary
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent = 4)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent = 4) #dumps() converts a python object into a json formatted String

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