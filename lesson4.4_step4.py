from selenium import webdriver
import time

import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector(".btn").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
   
    answer=browser.find_element_by_id("answer")
    answer.send_keys(y)
        
    button = browser.find_element_by_css_selector(".btn")
    button.click()
finally:
    time.sleep(7)
    browser.quit()

