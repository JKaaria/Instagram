from InstagramAPI import InstagramAPI

# Login to your Instagram account
username = 'ucaptrading'
password = 'Proptrading&2120'
api = InstagramAPI(username, password)
api.login()

# Get the media ID of the post you want to extract likes from
media_id = 'CloWxWrN8Yz'

# Get the list of users who liked the post
api.getMediaLikers(media_id)
users = api.LastJson['users']

# Open a text file for writing
with open('likes.txt', 'w') as f:

    # Loop through the list of users and extract their username and follower count
    for user in users:
        username = user['username']
        user_id = user['pk']
        api.getUsernameInfo(user_id)
        user_info = api.LastJson['user']
        follower_count = user_info['follower_count']
        result = f"{username}, {follower_count}\n"
        f.write(result)
        print(result)

# Close the text file
f.close()

# Logout from your Instagram account
api.logout()
