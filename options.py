# CHANGE YOUR PROFILE PATH HERE
profile_path = "C://Users/julie/AppData/Local/Google/Chrome/User Data/Default"

# for the pattern recognition (they are the boundaries on the width axis that contain the send arrow)
y1,y2 = 480, 520
x1,x2 = 120,140

# where to click
SEARCH = (740,142)
ENTER = (740,200)
FOLLOW = (972,209)
CONFIRM = (766,536)

import numpy as np
def find_pattern(im,pattern) :
    for i in range(im.shape[0] - pattern.shape[0]) :
        if np.linalg.norm(im[i:i+ pattern.shape[0],y1:y2,:]-pattern) <  20 :
            return i
    return None

def find_follow(im,pattern) :
    for i in range(im.shape[1] - pattern.shape[1]) :
        if np.linalg.norm(im[x1:x2,i:i+ pattern.shape[1],:]-pattern) <  20 :
            return i
    return None

def find_blue(im) :
    for i in range(im.shape[1]) :
        if im[int((x1+x2)//2),i,2] > 200 and im[int((x1+x2)//2),i,0] < 100 :
            return i

def mouse_to_browser(x,y) :
    return int(x/888 * (822-102)) + 102,int(y / 1920 * 1535)