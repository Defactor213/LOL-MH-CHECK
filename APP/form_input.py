from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = r"C:\Users\User\Desktop\FILES\Projects\MH Checker\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://matchhistory.sg.leagueoflegends.com/en/#page/landing-page")
time.sleep(2)
search = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/input")
#best to search for id > class > name 
search.send_keys("defactor213")
search.send_keys(Keys.RETURN)


