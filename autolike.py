from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from options import profile_path,y1,y2,find_pattern,mouse_to_browser
import numpy as np
from PIL import Image
from pynput.mouse import Button, Controller
import log
import sys

def click(x,y) :
    x,y = mouse_to_browser(x,y)
    mouse.position = (y,x) 
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(.1)
    # ActionChains(driver).move_by_offset(-x,-y).perform()


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

# how many posts are going to be liked
if len(sys.argv) == 2 :
    try :
        max_count = int(sys.argv[1])
    except :
        raise Exception("The argument is not an integer !")
else :
    max_count = 10_000

# To know when you finished
liked = 0
already_liked = 0
done = 0 # count how many pictures liked are in a row ==> ~10 and the loop is broken
while done < 10  and liked < max_count :
    # screen shot the current page
    driver.get_screenshot_as_file("./screenshots/screenshot.png")
    # open the result
    im = np.array(Image.open("./screenshots/screenshot.png"))[:,:,:3]
    # find whether the patter is here
    to_like = find_pattern(im,pattern)
    if to_like :
        color = im[to_like + 15 , y1 - 80]
        if color[0] > 200 and color[1] < 100  :
            # print("Already liked")
            done += 1
            already_liked += 1
        else : 
            click(to_like + 15,y1 - 80)
            liked += 1
            done = 0
            print("Like")
            
    # else : 
        # print("Nothing to see here")
    # scroll down
    driver.execute_script("window.scrollBy(0, 400)")
    time.sleep(.2)

driver.quit()
print("Liked {} photos.".format(liked))