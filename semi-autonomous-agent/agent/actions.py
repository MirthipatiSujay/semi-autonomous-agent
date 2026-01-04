from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def search_topic(driver, topic="Artificial Intelligence"):
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.clear()
    search_box.send_keys(topic)
    search_box.send_keys(Keys.ENTER)
    sleep(3)
