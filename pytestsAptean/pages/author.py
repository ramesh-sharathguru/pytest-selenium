import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pytestsAptean.pages.base import BasePage, step_tracker

class AuthorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.author_article = (By.XPATH, "//app-author//div[@class='author-resource-list']")

        self.author_article_container = (By.XPATH, "//div[@class='author-resource-list']//div[contains(@class,'insights-card__content--wrap')]")

        self.author_name = (By.XPATH, ".//div[contains(@class,'resource-details')]")
        self.author_article_title = (By.XPATH, ".//div[contains(@class,'insights-card__title')]")

        # self.nxt_btn = (By.XPATH, "//button[@class= 'pagination-control-next']")
        self.nxt_btn = (By.CSS_SELECTOR, ".pagination-control-next")

        # self.author_article_title_element = (By.XPATH, "//div[contains(@class,'author-resources')]//div[contains(@class,'insights-card__title')]")

    def get_web_element(self,web_locator):
        try:
            time.sleep(2)
            web_element = self.driver.find_element(*web_locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", web_element)
            return web_element
        except Exception as e:
            print(f"[ERROR] Failed to scroll into view for locator {web_locator}: {e}")
            return None

    def get_web_elements(self, web_locators):
        try:
            time.sleep(2)
            web_elements = self.driver.find_elements(*web_locators)
            return web_elements
        except Exception as e:
            print(f"[ERROR] Failed to scroll into view for locator {web_locators}: {e}")
            return None

        # return self.driver.find_elements(*self.author_article_cards)

    def author_aptean_page(self):
        pagination_button_locator = self.driver.find_element(By.CSS_SELECTOR, ".pagination-control-next")

        txt_file_path = "author_article.txt"
        file = open(txt_file_path, "a", encoding="utf-8")

        while True:
            self.get_web_element(self.author_article)
            step_tracker.add_step(" Author Articles  ", " Reading author articles ")
            all_author_article_card = self.get_web_elements(self.author_article_container)

            for each_article in all_author_article_card:
                time.sleep(2)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", each_article)
                print(each_article.text)
                if 'Jack Payne' in each_article.text:
                    # file.write(f"Article {article_num} : ")
                    file.write("--" * 11, "PASS", "------" * 11)
                    file.write(each_article.text)
                    file.write("\n")
                    file.write("------"*26)
                    file.write("\n")
                else:
                    # file.write(f"Article {article_num} : ")
                    file.write("--"*11,"FAIL","------"*11)
                    file.write(each_article.text)
                    file.write("\n")
                    file.write("------"*26)

            time.sleep(2)

            try:
                # Wait for the button to be present
                pagination_button = WebDriverWait(self.driver, 10).until( EC.element_to_be_clickable(pagination_button_locator))
                time.sleep(4)
                if pagination_button.is_displayed() and pagination_button.is_enabled():
                    self.driver.execute_script("arguments[0].click();", pagination_button)
                else:
                    print("[ERROR] Failed to click pagination_button_locator")
                    break
            except Exception as e:
                print(f"[ERROR] Failed to click pagination_button_locator: {e}")
                file.close()
                break