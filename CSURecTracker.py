#   Author: Ryan Guidice
#   Description: Script to track CSU rec counts

import argparse
import time
from selenium import webdriver

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="CSU rec count tracker")
    parser.add_argument('-hl', '--headless', help="Run chrome webdriver in headless mode", action="store_true")
    args = parser.parse_args()
    if args.headless:
        headless = True
    else:
        headless = False
    chrome_options = webdriver.ChromeOptions()
    # Hide logging messages
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if headless:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://csurec.colostate.edu/facility/rec-cams/")

    time.sleep(5)

    metrics = driver.find_elements_by_xpath('//div[contains(@style,"text-align:center;")]')

    print(metrics)
