import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get('https://www.youtube.com/watch?v=mRe-514tGMg')
time.sleep(15)
ActionChains(browser).send_keys(Keys.SPACE).send_keys("f").perform()
time.sleep(15)
currentTime = time.strftime("%Y%m%d-%H%M%S")
browser.save_screenshot(f"./screenshots/screenshot_{currentTime}.png")
time.sleep(5)
browser.close()