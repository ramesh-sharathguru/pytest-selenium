import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from axe_selenium_python import Axe
from selenium.webdriver.common.by import By

from pytestsAptean.pages.industries import IndustriesPage

BASE_URL = "https://www.aptean.com/en-US"

# APTEAN_REGION = ['en-US', 'fr-CA', 'es-US', 'nl-NL', 'de-DE']

# @pytest.mark.skip(reason="This test is currently under development.") # ignore the below test for now
def test_aptean_industries(all_tests_driver):
    driver = all_tests_driver

    driver.get(BASE_URL)
    # driver.implicitly_wait(4)

    industry_obj = IndustriesPage(driver)

    industry_obj.industries_categories()
