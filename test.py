from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import urlparse
import sys
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

# setting general password
passwordStr = 'prueba12'

# opening chrome instance
browser = webdriver.Chrome(chrome_options=option)

# opening IDP in chrome
browser.get(('https://www.facebook.com/'))

	# clicking, clearing and filling username input
print('Finding username input...')
time.sleep(2) # waiting for input to appear
browser.find_element_by_id('email').click()
browser.find_element_by_id('email').send_keys('jared@impag.com.mx')
browser.find_element_by_id('pass').click()
browser.find_element_by_id('pass').send_keys('Proyecto#1')
browser.find_element_by_id('u_0_b').click()
# browser.find_element_by_xpath(//button[contains(.="Photo/Video")]).click()
browser.find_elements_by_xpath("//*[contains(text(), 'Photo/Video')]")