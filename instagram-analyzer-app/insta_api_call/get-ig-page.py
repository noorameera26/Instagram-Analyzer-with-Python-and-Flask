from get_token import getCreds, makeApiCall

def getInstaAccount(params):
    """
    Function to get facebook pages for a user

    API endpoint:
    https://graph.facebook.om/{graph-api-version}/{page-id}?access_token={your-access-token}
    &fields=instagram_business_account
    
    Returns:
    Object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'instagram_business_account'
    
    url = params['endpoint_base'] + params['page_id']

    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'no'
response = getInstaAccount(params)

print('\n---INSTAGRAM ACCOUNT INFO---\n')
print("Page ID:")
print(response['json_data']['id'])
print("Instagram Business Account ID:")
print(response['json_data']['instagram_business_account']['id'])