import time
from selenium.webdriver.common.by import By
from pytestsAptean.pages.base import BasePage, step_tracker

class IndustriesPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

        self.category_industry = (By.XPATH, "//header//button[@data-label='Industries']")
        self.food_beverage = (By.XPATH,"//app-sub-menu//div[contains(text(),' Food and Beverage ')]")
        self.food_beverage_bakery  = (By.XPATH, "//app-sub-menu//div/a[contains(text(),' Bakery ')]")
        self.food_beverage_beverages = (By.XPATH, "//app-sub-menu//div/a[contains(text(),' Beverages ')]")
        self.food_beverage_Confectionery = (By.XPATH, "//app-sub-menu//div/a[contains(text(),' Confectionery ')]")
        self.food_beverage_contract_manufacturing = (By.XPATH, "//app-sub-menu//div/a[contains(text(),' Contract Manufacturing ')]")
        self.food_beverage_dairy = (By.XPATH, "//app-sub-menu//div/a[contains(text(),' Dairy ')]")
        self.food_beverage_fresh_produce_and_farming = (By.XPATH, "//app-sub-menu//div/a[contains(text(),'Fresh Produce and Farming')]")
        self.food_beverage_frozen_and_prepared_packaged_foods = (By.XPATH, "//app-sub-menu//div/a[contains(text(),'Frozen and Prepared Packaged Foods')]")
        self.food_beverage_meat_seafood_poultry = (By.XPATH, "//app-sub-menu//div/a[contains(text(),'Meat, Seafood and Poultry')]")
        self.food_beverage_sauces_dressing = (By.XPATH, "//app-sub-menu//div/a[contains(text(),'Sauces and Dressings')]")
        self.food_beverage_snacks = (By.XPATH, "//app-sub-menu//div/a[contains(text(),'Snacks')]")
        self.food_beverage_spices_ingredients = (By.XPATH, "//app-sub-menu//div/a[contains(text(),'Spices and Ingredients')]")

    def scroll_into_view(self,web_loc):
        time.sleep(4)
        web_ele = self.driver.find_element(*web_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",web_ele)
        return web_ele


    def industries_categories(self):
        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_bakery).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_beverages).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_Confectionery).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_contract_manufacturing).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_dairy).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_fresh_produce_and_farming).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_frozen_and_prepared_packaged_foods).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_meat_seafood_poultry).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_sauces_dressing).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_snacks).click()

        self.scroll_into_view(self.category_industry).click()
        self.scroll_into_view(self.food_beverage).click()
        self.scroll_into_view(self.food_beverage_spices_ingredients).click()







