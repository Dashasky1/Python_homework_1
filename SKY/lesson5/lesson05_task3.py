from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://the-internet.herokuapp.com/inputs")

search_box = browser.find_element(By.CSS_SELECTOR, "input")

search_box.send_keys("123")

search_box.clear()

search_box.send_keys("456")

browser.quit()

