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