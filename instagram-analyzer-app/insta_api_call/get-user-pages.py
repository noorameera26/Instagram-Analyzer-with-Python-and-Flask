from get_token import getCreds, makeApiCall

def getUserPages(params):
    """
    Function to get facebook pages for a user

    API endpoint:
    https://graph.facebook.om/{graph-api-version}/me/accounts?access_token={access-token}
    
    Returns:
    """

    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + 'me/accounts' 

    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'yes'

response = getUserPages(params)