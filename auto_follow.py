from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from options import profile_path,y1,y2,find_pattern,mouse_to_browser,SEARCH,ENTER,FOLLOW,CONFIRM,x1,x2,find_follow,find_blue
import numpy as np
from PIL import Image
from pynput.mouse import Button, Controller
import sys
import keyboard

# left click to the given position
def click(x,y,modify=True) :
    if modify :
        x,y = mouse_to_browser(x,y)
    mouse.position = (y,x) 
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(.1)
    # ActionChains(driver).move_by_offset(-x,-y).perform()

# search for a person
def search(username) :
    click(SEARCH[1],SEARCH[0],modify=False)
    time.sleep(2)
    keyboard.write(username)
    time.sleep(2)
    click(ENTER[1],ENTER[0],modify=False)
    time.sleep(2)

# unfollow someone
def unfollow(username) :
    search(username)
    # screenshot
    driver.get_screenshot_as_file("./screenshots/screenshot.png")
    # open the result
    im = np.array(Image.open("./screenshots/screenshot.png"))[:,:,:3]
    # where is the sign
    i = find_follow(im,follow_sign)
    if i == None :
        return
    click(int((x1+x2)//2),i,modify=True)
    time.sleep(1)
    click(CONFIRM[1],SEARCH[0],modify=False)
    time.sleep(1)

# follow someone
def follow(username) :
    search(username)
    # screenshot
    driver.get_screenshot_as_file("./screenshots/screenshot.png")
    # open the result
    im = np.array(Image.open("./screenshots/screenshot.png"))[:,:,:3]
    # where is the sign
    i = find_blue(im)
    if i == None : return
    click(int((x1+x2)//2),i + 30,modify=True)
    time.sleep(1)

# load the pattern
follow_sign = np.array(Image.open("./data/follow.png"))
    
# Create the options
options = webdriver.ChromeOptions()
# Add your chrome profile (to remember you) and specify full screen
options.add_argument("user-data-dir={}".format(profile_path)) #Path to your chrome profile
options.add_argument("--start-maximized")
options.add_argument('log-level=3')

# Run the driver
driver = webdriver.Chrome(options=options)

# Create the mouse
mouse = Controller()

# load the pattern
pattern = np.array(Image.open("./data/pattern.png"))

# Open instagram
driver.get('https://www.instagram.com/?hl=fr')
time.sleep(3)

if __name__ == '__main__':
    follow("rossgeller")
    follow("chandler_thegolden")