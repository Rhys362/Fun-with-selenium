from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#open in headless mode
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.get('https://www.sundaytimeswineclub.co.uk/')

sleep(2)

#accept cookie 
cookie_button = browser.find_element_by_xpath("//button[text()='Accept Cookies']")
cookie_button.click()

sleep(2)

#hit login
#probably bad practice to use xpath in this way but for my own use it is easy to maintain if site is changed
login_button = browser.find_element_by_xpath("/html/body/div[4]/header/div[4]/div/div[5]/div[1]/div/div[2]/div[1]/span/a")
login_button.click()

sleep(2)

#login details
browser.find_element_by_id("email").send_keys("email/user goes here")

actions = ActionChains(browser)
actions.send_keys(Keys.TAB)
actions.perform()
element = browser.switch_to.active_element
element.send_keys("password goes here")

accept_button = browser.find_element_by_xpath("//button[text()='Log in']")
accept_button.click()

sleep(2)

#navigate to account/wine plan
#same again regarding xpath, don't think it should be done like this but for my purposes it works. Will fix if breaks. For future could add an alert which notifies me if script fails due to page update?
browser.find_element_by_xpath("/html/body/div[4]/header/div[4]/div/div[5]/div[1]/div/div[2]/div[2]/span[1]/a").click()
browser.find_element_by_link_text('Wine Plans').click()

#find button with push back id
element = WebDriverWait(browser, 10).until(
EC.presence_of_element_located((By.ID, "push-back")))
element.click()

#scroll to 4th menu option
n = 4
actions = ActionChains(browser)
actions.send_keys(Keys.ARROW_DOWN * n)
actions.perform()
#enter
n = 1
actions = ActionChains(browser)
actions.send_keys(Keys.ENTER * n)
actions.perform()

#exit
browser.quit()
