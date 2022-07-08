from get_token import getCreds, makeApiCall
import datetime #import the time our access token expires into a readable format

def debugAccessToken(params):
    """
    To get info on an access token

    API endpoint:
        https://graphs.facebook.com/
        debug_token?input_token={input-token}&access_token={valid-access-token}
    
    Returns:
        object: data from the endpoint
    """

    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = params['access_token']
    url = params['graph_domain'] + '/debug_token'

    return makeApiCall(url, endpointParams, params['debug'])
    
params = getCreds()
params['debug'] = 'yes'
response = debugAccessToken(params)

print("\nExpires at: ")
print(datetime.datetime.fromtimestamp(response['json_data']['data']['data_access_expires_at']))
