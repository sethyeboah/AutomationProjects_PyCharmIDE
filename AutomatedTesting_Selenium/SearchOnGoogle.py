# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Here Chrome will be used
driver = webdriver.Chrome()

# URL of website
url = "https://www.google.com/"

#maximize browser
driver.maximize_window()

# Opening the website
driver.get(url)

# # Input Text In Search Box By Finding Element Name
# inputTextInSearchBox = driver.find_element("name", "q")
# inputTextInSearchBox.send_keys("LinkedIn Login")
# inputTextInSearchBox.send_keys(Keys.ENTER)

# Input Text In Search Box Using Xpath
# inputTextInSearchBox = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# inputTextInSearchBox = driver.find_element(By .XPATH, "//input[@class='gLFyf gsfi']")
inputTextInSearchBox = driver.find_element(By .XPATH, "//div[@class='a4bIc']/input[1]")
inputTextInSearchBox.send_keys("Facebook Login")
inputTextInSearchBox.send_keys(Keys.ENTER)

time.sleep(5)
driver.close()