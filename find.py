import os
from datetime import datetime
import re
from auto_follow import *
import log

def is_latter(current_date,other) :
    current_value = current_date.split("_")
    other_value = other.split("_")
    if other_value[2] > current_value[2] : # Year
        return True
    elif other_value[2] == current_value[2] and other_value[1] > current_value[1] : # Month
        return True
    elif other_value[2] == current_value[2] and other_value[1] == current_value[1] and other_value[0] > current_value[1] : # Day
        return True

for dir in os.listdir(".") :
    if os.path.isdir(dir) :
        if re.findall("\d\d_\d\d_\d\d\d\d",dir) != [] :
            try :
                if is_latter(current_dir,dir) :
                    current_dir = dir
            except :
                current_dir = dir

print("Working with the date {}.".format(current_dir.replace("_"," ")))

# they follow but I don't
with open(os.path.join(current_dir,"to_follow.txt"),"r") as f :
    to_follow = f.readlines()

# I follow but they don't
with open(os.path.join(current_dir,"non_returned.txt"),"r") as f :
    non_returned = f.readlines()

# They follow but do not like any posts
with open(os.path.join(current_dir,"ghost.txt"),"r") as f :
    ghosts = f.readlines()

"""print("We now follow :")
for foll in to_follow :
    print(foll)
    follow(foll)
    break"""

"""print("We unfollow (they did not follow back) :")
for non in non_returned :
    print(non)
    unfollow(non)
    break"""

"""print("We unfollow (they did not like any posts) :")
for ghost in ghosts :
    print(ghost)
    unfollow(ghost)
    break"""
