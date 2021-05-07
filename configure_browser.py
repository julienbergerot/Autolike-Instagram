from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from options import profile_path

# Create the options
options = webdriver.ChromeOptions()
# Add your chrome profile (to remember you) and specify full screen
options.add_argument("user-data-dir={}".format(profile_path)) #Path to your chrome profile
options.add_argument("--start-maximized")
options.add_argument('log-level=3')

# Run the driver
driver = webdriver.Chrome(options=options)

# Open instagram
driver.get('https://www.instagram.com/?hl=fr')

# To know when you finished
x = input("Enter once you have succcessfully logged in and accepted all the cookies.")
time.sleep(1)

driver.quit()
print("Configuration done")