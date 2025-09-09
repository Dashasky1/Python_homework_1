
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get(" http://the-internet.herokuapp.com/login")

search_box = browser.find_element(By.CSS_SELECTOR, "input#username")
search_box.send_keys("tomsmith")

search_box = browser.find_element(By.CSS_SELECTOR, "input#password")
search_box.send_keys("SuperSecretPassword!")

search_box = browser.find_element(By.CSS_SELECTOR, "button.radius")
search_box.send_keys(Keys.ENTER)

element_present = WebDriverWait(browser, 50).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

raw_text = element_present.text
print(raw_text)

browser.quit()
