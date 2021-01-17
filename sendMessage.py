import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver
from fake_useragent import UserAgent
import user
from selenium.webdriver.chrome.options import Options
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=selenium")
options.add_argument(f"user-agent={useragent.random}")
driver = selenium.webdriver.Chrome()
chrome_options = Options()

def login():
    driver.get("https://instagram.com")
    time.sleep(1)
    email_input = driver.find_element_by_name("username")
    email_input.clear()
    email_input.send_keys(f"{user.login}")
    time.sleep(1)
    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(f"{user.password}")
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(1)
    pickle.dump(driver.get_cookies(), open(f"{user.login}_cookies","wb"))
    cookies = pickle.load(open(f"{user.login}_cookies", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(5)
    not_now = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div")
    not_now.click()
    time.sleep(1)
    not_now2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    not_now2.click()
    pass

def sendMassage(name,txt,number):
    driver.get(f"https://www.instagram.com/{name}/")
    time.sleep(1)
    msBt = driver.find_element_by_class_name("sqdOP")
    msBt.click()
    time.sleep(4)
    textarea = driver.find_element_by_tag_name("textarea")
    textarea.clear()
    i = 0

    while i < number:
        textarea.send_keys(f"{txt}")
        textarea.send_keys(Keys.ENTER)
        i = i+1
def close():
    driver.close()
    driver.quit()
    pass
