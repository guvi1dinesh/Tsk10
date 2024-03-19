## USING PYTHON SELENIUM AUTOMATION AND THE URL: https://www.instagram.com/guviofficial/
# KINDLY DO THE FOLLOWING MENTIONED TASKS:-
### (1) USE EITHER RELATIVE OR ABSOLUTE XPATH ONLY FOR THE TASK.
### (2) EXTRACT THE TOTAL NUMBER OF FOLLOWERS AND FOLLOWING FROM THE URL MENTIONED ABOVE.




from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.instagram.com/guviofficial/")


sleep(10)
follower = driver.find_element(by=By.XPATH, value = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span')
print(follower.text)


following = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span')
print(following.text)


driver.quit()

