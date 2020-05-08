import time
from csv import writer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def write_viewers_to_csv(views):
    views_splitted = views.split(" ")

    with open("./views.csv", 'a+', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow([time.strftime("%Y-%m-%d %H:%M"), views_splitted[0]])

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
try:
    browser.get('https://www.youtube.com/watch?v=mRe-514tGMg')
    time.sleep(10)

    ActionChains(browser).send_keys(Keys.SPACE).send_keys("f").perform()
    time.sleep(10)

    currentTime = time.strftime("%Y%m%d-%H%M")
    browser.save_screenshot(f"./screenshots/screenshot_{currentTime}.png")
    views = browser.find_element_by_class_name("view-count")

    write_viewers_to_csv(views.text)
    time.sleep(5)
    
    print("done")
finally:
    browser.quit()
    print("driver disposed")

