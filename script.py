from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time


# Read the contents of the file
with open('file.txt', 'r') as f:
    file_contents = f.read()

# Retrieve Login route and credentials from file
login_url = file_contents.split('\n')[0].split('=')[1].strip().strip("'")
username = file_contents.split('\n')[1].split('=')[1].strip().strip("'")
password = file_contents.split('\n')[2].split('=')[1].strip().strip("'")


# Initialize the Chrome webdriver and navigate to the login page
# Pls replace this with your driver path
chromedriver_path = '..\Downloads\chromedriver_win32'

# Create a Service object with the chromedriver path
service = Service(chromedriver_path)

# Pass the Service object to the webdriver.Chrome method
driver = webdriver.Chrome(service=service)

driver.get(login_url)

# This tell selenium to fill in the following details and use the submit as well
user_field = driver.find_element(By.NAME,'phone_login')
user_field.send_keys(username)

pass_field = driver.find_element(By.NAME,'phone_pass')
pass_field.send_keys(password)

pass_field.send_keys(Keys.RETURN) #This will submit the form


# Login the second time using same credentials
user_field_ = driver.find_element(By.NAME,'VD_login')
user_field_.send_keys(username)

pass_field_ = driver.find_element(By.NAME,'VD_pass')
pass_field_.send_keys(password)

pass_field_.send_keys(Keys.RETURN)

# This tell selenium to "Hit ente  keyr" to display the select error
campg_field_ = driver.find_element(By.NAME,'VD_campaign')
campg_field_.send_keys(Keys.RETURN)

# Wait up to 10 seconds for the campg_field_ to be visible in order to display an error.
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.NAME, 'VD_campaign')))

# Get the value of the Campaign Select tag
soup = BeautifulSoup(driver.page_source, 'html.parser')
select_element = soup.find('select', id='VD_campaign')
options = select_element.find_all('option')
for option in options:
	# Loop through the option tags and print the error output
    print(f"Error-Output: {option.text}")

# Close the browser window
driver.quit()

