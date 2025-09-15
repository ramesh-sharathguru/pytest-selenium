import time
import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

TARGET_URL = "https://aptean-website-dev.azurewebsites.net/fr-CA/discrete-solution"


def test_functionality(general_driver):
    print("Page alignment test- SUCCESSFUL..!! ")
    driver = general_driver
    driver.get("TARGET_URL")
    time.sleep(4)
    assert "Discrete Manufacturing Solution" in driver.title

def test_performance(general_driver):
    driver = general_driver
    driver.get("TARGET_URL")
    timing = driver.execute_script("return window.performance.timing")
    load_time = timing["loadEventEnd"] - timing["navigationStart"]
    print(f"Performance test : {load_time} seconds")
    assert load_time > 3000

def test_ui_element(general_driver):
    print("assert header")
    driver = general_driver
    driver.get(TARGET_URL)
    time.sleep(4)


def test_responsive(general_driver):
    print("mobile window")
    driver = general_driver
    driver.set_window_size(375, 667)
    driver.get("TARGET_URL")
    time.sleep(20)
    assert driver.find_element(By.XPATH, "//app-contentful").is_displayed()

