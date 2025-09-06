
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get(" http://the-internet.herokuapp.com/login")

search_box = browser.find_element(By.CSS_SELECTOR, "input#username")
search_box.send_keys("tomsmith")

search_box = browser.find_element(By.CSS_SELECTOR, "input#password")
search_box.send_keys("SuperSecretPassword!")

search_box = browser.find_element(By.CSS_SELECTOR, "button.radius")
search_box.send_keys(Keys.ENTER)

search_box = browser.find_element(By.CSS_SELECTOR, "div#flash-messages").text

print()

browser.quit()