from selenium import webdriver
import time

browser = webdriver.Chrome('/usr/local/chromedriver')
browser.get('https://www.deviantart.com/users/login')
user = browser.find_element_by_name("username")
user.send_keys("user")
password = browser.find_element_by_name("password")
password.send_keys("pas")
login = browser.find_element_by_id("loginbutton")
login.click()
browser.get('https://www.deviantart.com/dshanti/modals/mygroups/')
groups = browser.find_elements_by_class_name("mygroup")
i = 0;
while i < len(groups) :
    browser.get('https://www.deviantart.com/dshanti/modals/mygroups/?offset=300')
    groups = browser.find_elements_by_class_name("mygroup")
    groups[i].click()
    time.sleep(5)
    #browser.switch_to.window(browser.window_handles[1 + i])
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    print(browser.current_url)
    browser.get(browser.current_url + 'gallery/?new')
    time.sleep(5)
    choice = browser.find_elements_by_xpath("//div[@collect_rid='1:857818331']")
    choice[0].click()
    submit = browser.find_element_by_xpath("//span[@class='ok-label']")
    try:
        submit.click()
    finally:
        print(i)
    i = i + 1
