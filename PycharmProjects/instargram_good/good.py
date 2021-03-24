from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time
url = 'http://www.imstagram.com'
driver = webdriver.Chrome('C:\Temp\chromedriver.exe')
driver.get(url)

time.sleep(1)

ID = 'pic._.caso'
PW = 'pp112233@'
try:
    login_id = driver.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = driver.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(3)

    popup2 = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    popup2.send_keys(Keys.ENTER)
    time.sleep(1)
    popup1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    popup1.send_keys(Keys.ENTER)


    search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div')
    search.send_keys("사진계정맞팔")
    search.send_keys(Keys.RETURN)

    el_list = driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]')
    el_list.click()

except Exception as e:
    print(e)
finally:
    print("finish")

