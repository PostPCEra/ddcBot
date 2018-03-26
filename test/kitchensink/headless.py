
# ----- steps for selenium
# 0. Be in virtual env with $. env/bin/activate
#  $pip install selenium
#  $pip show selenium    -- will show where it is installed
#   add it to path as shown below

#  do same for other webdriver and other packages
# ------------------------

import sys
sys.path.append('../env/lib/python3.5/site-packages')

from pathlib import Path

# code ref: https://medium.com/@pyzzled/running-headless-chrome-with-selenium-in-python-3f42d1f5ff1d
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
#chrome_driver = os.getcwd() +"\\chromedriver.exe"


chrome_driverpath = Path.cwd() / ".." / "env/bin/chromedriver"
print(chrome_driverpath)

# go to Google and click the I'm Feeling Lucky button
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driverpath)
driver =  webdriver.Chrome()
#driver.get("https://www.google.com")
driver.get("http://127.0.0.1:5000/runpy")

#lucky_button = driver.find_element_by_css_selector("[name=btnI]")
#lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")