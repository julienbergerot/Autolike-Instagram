# Get instance
import instaloader
from datetime import datetime
import os

# Check if already ran today
date = datetime.now().strftime("%d/%m/%Y").replace("/","_")
assert not os.path.isdir(str(date)) , "You already ran the program today."
# create the directory
os.mkdir(str(date))

L = instaloader.Instaloader()

# Login or load session
username = "username"
password = "password"
L.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# List of followers
print("Saving followers")
with open("./{}/followers.txt".format(str(date)),"w") as f :
    followers = set(profile.get_followers())
    for follower in followers :
        f.writelines(follower.username + "\n")

# List of followees
print("Saving followees")
with open("./{}/following.txt".format(str(date)),"w") as f :
    followees = set(profile.get_followees() )
    for follow in followees:
        f.writelines(follow.username + "\n")

# Non returned by them
print("Saving non returned")
non_back = followees - followers
with open("./{}/non_returned.txt".format(str(date)),"w") as f :
    for user in non_back :
        f.writelines(user.username + "\n")

# Oups we did not liked them back
print("Saving oupsies")
oupsies = followers - followees
with open("./{}/to_follow.txt".format(str(date)),"w") as f :
    for user in oupsies :
        f.writelines(user.username + "\n")

# Likes
likes = set() 
for post in profile.get_posts() : 
    likes = likes | set(post.get_likes())

# Ghost
print("Saving ghosts")
ghosts = followers - likes
with open("./{}/ghost.txt".format(str(date)),"w") as f :
    for ghost in ghosts :
        f.writelines(ghost.username + "\n")