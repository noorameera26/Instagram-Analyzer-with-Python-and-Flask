from get_token import getCreds, makeApiCall
import sys
import json

def getHashTagInfo(params):
    """
    Function to get info on a hashtag

    API endpoint:
    https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q=
    {hashtag-name}&fields={fields}

    Returns:
    Object: Data from the endpoint
    """
    endpointParams = dict()
    endpointParams['user_id'] = params['instagram_account_id']
    endpointParams['q'] = params['hashtag_name']
    endpointParams['fields'] = 'id,name'
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + 'ig_hashtag_search'

    return makeApiCall(url, endpointParams, params['debug'])


def getHashTagMedia(params):
    """
    Function to get posts on a hashtag

    API endpoint:
    https://graph.facebook.com/{graph-api-version}/{ig_hashtag_id}/top_media?user_id={user-id}&fields={fields}
    https://graph.facebook.com/{graph-api-version}/{ig_hashtag_id}/recent_media?user_id={user-id}&fields={fields}
    
    Returns:
    Object: Data from the endpoint
    """
    endpointParams = dict()
    endpointParams['user_id'] = params['instagram_account_id']
    endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type']

    return makeApiCall(url, endpointParams, params['debug'])

#get hashtag argument
try:
    hashtag = sys.argv[1] 
    #get first CLI argument if it's entered
    #note: sys.argv is a list in python that contains all the command line arguments
    #i.e. ['script-name.py', 'arg1', 'arg2', 'arg3'] 
except:
    hashtag = 'coding' #default hashtag

#make api call to endpoint to query hashtag id
params = getCreds()
params['hashtag_name'] = hashtag
response = getHashTagInfo(params)
params['hashtag_id'] = response['json_data']['data'][0]['id']

print('---- Hashtag Info----')
print('\nHashtag:', response['json_data']['data'][0]['name'])
print('\nHashtag ID:', response['json_data']['data'][0]['id'])

#make api call to endpoint to query top media
print('\n\n---- Hashtag Top Media----\n')
params['type'] = 'top_media'
topmediaresponse = getHashTagMedia(params)
print(json.dumps(topmediaresponse['json_data']['data'][0], indent=4))

# for post in topmediaresponse['json_data']['data']:
#     print("\n\n-----Post----\n")
#     print("Link to post:") #label
#     print(post['permalink']) #link to post
    
#     #print("\nPost Caption:") #label
#     #print(post['caption']) #post caption
#     print('\nMedia type:') #label
#     print(post['media_type']) #type of media
#     print("\nPosted at:") #label
#     #print(post['posted_at']) #when it was posted

# #make api call to endpoint to query latest media
# print('\n\n---- Hashtag Recent Media----\n')
# params['type'] = 'recent_media'
# recentmediaresponse = getHashTagMedia(params)

# for post in recentmediaresponse['json_data']['data']:
#     print("\n\n-----Post----\n")
#     print("Link to post:") #label
#     print(post['permalink']) #link to post
#     #print("\nPost Caption:") #label
#     #print(post['caption']) #post caption
#     print('\nMedia type:') #label
#     print(post['media_type']) #type of media
#     print("\nPosted at:") #label
#     #print(post['timestamp']) #when it was posted
