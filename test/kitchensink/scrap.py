
# ----- steps for selenium
# 0. Be in virtual env with $. env/bin/activate
#  $pip install selenium
#  $pip show selenium    -- will show where it is installed
#   add it to path as shown below

#  do same for other webdriver and other packages
# ------------------------

import sys
sys.path.append('../env/lib/python3.5/site-packages')

# code ref: https://stackoverflow.com/questions/39197977/python-beautifulsoup-scrape-yahoo-finance-value
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://finance.yahoo.com/quote/AAPL/profile?p=AAPL")

# wait for the Full Time Employees to be visible
wait = WebDriverWait(driver, 10)
employees = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[. = 'Full Time Employees']/following-sibling::strong")))
print(employees.text)

driver.close()