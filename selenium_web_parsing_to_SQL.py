#Get data from website and store in SQL database

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import mysql.connector


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.barnesandnoble.com/w/effective-python-brett-slatkin/1130203296?ean=9780134853987")
time.sleep(5)

isbn = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[1]/td").get_attribute("innerHTML")
publisher = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[2]/td/a/span").get_attribute("innerHTML")
pubDate = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[3]/td").get_attribute("innerHTML")
series = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[4]/td/a").get_attribute("innerHTML")
edition = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[5]/td").get_attribute("innerHTML")
pages = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[6]/td").get_attribute("innerHTML")
salesRank = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[7]/td").get_attribute("innerHTML")
dims = driver.find_element_by_xpath("//*[@class='plain centered']/tbody[1]/tr[8]/td").get_attribute("innerHTML")
width = dims[0:5]
height =  dims[10:15]
depth = dims[20:25]
price = driver.find_element_by_xpath("//*[@id='formatSelect-option-0']/a").get_attribute("innerHTML")[-6:]

driver.quit()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    autocommit=True
)


mycursor = mydb.cursor()

#Create database
mycursor.execute("CREATE DATABASE technicalinterview")
mycursor.close()

mytable = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="technicalinterview",
    autocommit=True
)

newcursor = mytable.cursor()
#Create table
table = "CREATE TABLE book (ISBN13 VARCHAR(255),Publisher VARCHAR(255),PublicationDate VARCHAR(255), Series VARCHAR(255), EditionDescription VARCHAR(255), Pages VARCHAR(255),SalesRank VARCHAR(255),ProductWidth VARCHAR(255),ProductHeight VARCHAR(255), ProductDepth VARCHAR(255),Price VARCHAR(255))"
newcursor.execute(table)

#Insert data
data = "INSERT INTO technicalinterview.book (ISBN13, Publisher, PublicationDate, Series, EditionDescription, Pages, SalesRank, ProductWidth, ProductHeight, ProductDepth, Price) VALUES ('"+isbn+"', '"+publisher+"', '"+pubDate+"', '"+series+"', '"+edition+"', '"+pages+"', '"+salesRank+"', '"+width+"', '"+height+"', '"+depth+"', '"+price+"')"
newcursor.execute(data)
newcursor.close()
mydb.close()
