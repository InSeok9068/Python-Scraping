from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(executable_path='C:/Users/Lee In Seok/PythonScraping/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()