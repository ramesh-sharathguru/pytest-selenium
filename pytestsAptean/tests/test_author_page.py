import time
import pytest
import pytest_html
import pytest_assume
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pytestsAptean.pages.author import AuthorPage

BASE_AUTHOR_PAGE = "https://aptean-website-dev.azurewebsites.net/en-US/author/jack-payne-test"

def test_author_page(all_tests_driver):
    driver = all_tests_driver
    driver.get(BASE_AUTHOR_PAGE)

    author_page_obj = AuthorPage(driver)

    author_page_obj.author_aptean_page()

