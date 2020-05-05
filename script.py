import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/watch?v=mRe-514tGMg')
time.sleep(5)
ActionChains(browser).send_keys(Keys.SPACE).send_keys("f").perform()
time.sleep(5)
currentTime = time.strftime("%Y%m%d-%H%M%S")
browser.save_screenshot(f"screenshot_{currentTime}.png")
print("done")
browser.close()