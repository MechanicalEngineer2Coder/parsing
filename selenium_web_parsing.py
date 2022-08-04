from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('''Enter website address or html file location and name here''')

print(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/div[2]/ul[1]/li[1]').text)
print(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/div[2]/ul[1]/li[2]').text)
print(driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/h3').text)

driver.quit()
