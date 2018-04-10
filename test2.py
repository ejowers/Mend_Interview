import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Function to logout
def logout():
    # Locate and click user menu icon
    user_menu = browser.find_element_by_id("dropdown-toggle")
    user_menu.click()
    
    # Locate and click "Log Out" item
    log_out = browser.find_element_by_id("sign-out-link")
    log_out.click()
    
    # Return to login page
    browser.get('https://www.codecademy.com/login')
    return;

## Setup browser and navigate to codecademy.com
chromedriver = '/Users/ejowers/Software/Selenium/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.codecademy.com/login')

## Test 1 - Successful Test using correct credentials
# Locate the username, password, and submit button fields
username = browser.find_element_by_id("user_login")
password = browser.find_element_by_id("login__user_password")
submit_button = browser.find_element_by_id("user_submit")

# Clear username field and enter correct username
username.clear()
username.send_keys("usr1234")

# clear password field and enter correct password
password.clear()
password.send_keys("Password1234")

# Click the 'Log In' button
submit_button.click()

## Logout
logout()

## Test 2 - Failed Test using incorrect credentials
# Locate test fields
username = browser.find_element_by_id("user_login")
password = browser.find_element_by_id("login__user_password")
submit_button = browser.find_element_by_id("user_submit")

# Clear username field and enter incorrect username
username.clear()
username.send_keys("usr123")

# Clear password field and enter correct password
password.clear()
password.send_keys("Password1234")

# Click the 'Log In' button
submit_button.click()
