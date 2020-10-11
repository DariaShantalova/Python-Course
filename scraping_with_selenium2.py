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
browser.get('https://www.deviantart.com/deviation/857610701/groups')
groups = browser.find_elements_by_xpath("//span[@class='grpicon']")
i = 0;
while i < len(groups) :
    browser.get('https://www.deviantart.com/deviation/857610701/groups')
    groups = browser.find_elements_by_xpath("//span[@class='grpicon']")
    groups[i].click()
    i = i + 1;

    join = browser.find_elements_by_xpath("//i[@class='icon i23']")
    if len(join) > 1 :
        join[1].click()
        time.sleep(3)
        try :
            send = browser.find_element_by_xpath("//*[text()='Submit Request']")
            send.click()
            time.sleep(3)
        except Exception:
            print('bad group')
        finally:
            print('bag group', i)

browser.quit()

