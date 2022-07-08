from get_token import getCreds, makeApiCall

def getLongLivedAccessToken(params):
    """
    Function to get long lived access token

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=
        fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
    
    Returns:
        Object: data from the endpoint
    """

    endpointsParams = dict()
    endpointsParams['grant_type'] = 'fb_exchange_token'
    endpointsParams['client_id'] = params['client_id']
    endpointsParams['client_secret'] = params['client_secret']
    endpointsParams['fb_exchange_token'] = params['access_token']
    
    url = params['endpoint_base'] + 'oauth/access_token'

    return makeApiCall(url, endpointsParams, params['debug'])

params = getCreds()
params['debug'] = 'yes'
response = getLongLivedAccessToken(params)

print("\n ---- ACCESS TOKEN INFO --- \n")
print("Long Lived Access Token:")
print(response['json_data']['access_token'])
    