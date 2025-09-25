import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from axe_selenium_python import Axe
from selenium.webdriver.common.by import By

from pytestsAptean.pages.industries import IndustriesPage
from pytestsAptean.pages.base import step_tracker

BASE_URL_PROD = "https://www.aptean.com/en-US"
BASE_URL = "https://aptean-website-dev.azurewebsites.net/en-US"

# APTEAN_REGION = ['en-US', 'fr-CA', 'es-US', 'nl-NL', 'de-DE']

# @pytest.mark.skip(reason="This test is currently under development.") # ignore the below test for now
def test_aptean_industries(all_tests_driver):
    driver = all_tests_driver

    driver.get(BASE_URL)
    # driver.implicitly_wait(4)
    step_tracker.add_step("Test started", f"base 'url' {BASE_URL}")

    industry_obj = IndustriesPage(driver)

    industry_obj.industries_categories()
