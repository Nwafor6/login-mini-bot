from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

# Login route and credentials
login_url = 'https://dialer018.talkasiavoip.cc/agc/vicidial.php'
username = '8000'
password = '123qwe123'

# Initialize the Chrome webdriver and navigate to the login page
driver = webdriver.Chrome('..\Downloads\chromedriver_win32')# Pls replace this with your driver path
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
print(options,"options")
for option in options:
	# Loop through the option tags and print the error output
    print(option.text,"Hello")



# Keep the browser window open for 1min
time.sleep(60)




# Close the browser window
# driver.quit()

