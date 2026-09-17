from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.constance-de-salm.de/archiv/#/document/2")
wait = WebDriverWait(driver, 10)
elem = driver.find_element(By.PARTIAL_LINK_TEXT, "Abschrift")
print(elem)
driver.close()
