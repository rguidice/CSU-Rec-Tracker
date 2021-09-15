#   Author: Ryan Guidice
#   Description: Script to track CSU rec counts

import argparse
from selenium import webdriver

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="CSU rec count tracker")
    parser.add_argument('-hl', '--headless', help="Run chrome webdriver in headless mode", action="store_true")
    args = parser.parse_args()
    # username = args.username
    # password = args.password
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

    metrics = driver.find_elements_by_css_selector("text-align:center;")

    print(metrics)
