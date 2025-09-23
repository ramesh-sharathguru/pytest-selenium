# ============= pages/base_page.py =============
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class StepLogger:
    """Simple step tracking for HTML reports"""

    def __init__(self):
        self.step_number = 0
        self.all_steps = []

    def add_step(self, what_happened, details=""):
        """Add a step to our report"""
        self.step_number += 1
        step = {
            'number': self.step_number,
            'action': what_happened,
            'details': details,
            'status': 'PASS'
        }
        self.all_steps.append(step)
        print(f"Step {self.step_number}: {what_happened}")
        if details:
            print(f" Details: {details}")

    def get_all_steps_html(self):
        """Create HTML table of all steps"""
        html = "<h3>Test Steps:</h3><table border='1'>"
        html += "<tr><th>Step</th><th>Action</th><th>Details</th><th>Status</th></tr>"

        for step in self.all_steps:
            html += f"<tr>"
            html += f"<td>{step['number']}</td>"
            html += f"<td>{step['action']}</td>"
            html += f"<td>{step['details']}</td>"
            html += f"<td>{step['status']}</td>"
            html += f"</tr>"

        html += "</table>"
        return html


# Create one logger for the whole test
step_tracker = StepLogger()


class BasePage:
    """Common functions that all pages can use"""

    def __init__(self, driver):
        self.driver = driver
        self.wait_time = float(os.getenv('SLEEP_TIME', '0'))

    def wait_to_see(self):
        """Pause so you can see what's happening"""
        if self.wait_time > 0:
            time.sleep(self.wait_time)

    def find_element_safely(self, how_to_find):
        """Find element and log the step"""
        self.wait_to_see()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(how_to_find)
        )
        step_tracker.add_step("Found element", f"Looking for: {how_to_find}")
        return element

    def click_element(self, how_to_find):
        """Click element and log the step"""
        self.wait_to_see()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(how_to_find)
        )
        element.click()
        step_tracker.add_step("Clicked element", f"Clicked: {how_to_find}")
        self.wait_to_see()

    def type_text(self, how_to_find, text):
        """Type text and log the step"""
        self.wait_to_see()
        element = self.find_element_safely(how_to_find)
        element.clear()
        element.send_keys(text)
        step_tracker.add_step("Typed text", f"Typed '{text}' into {how_to_find}")
        self.wait_to_see()

    def go_to_page(self, url):
        """Go to a page and log the step"""
        self.driver.get(url)
        step_tracker.add_step("Opened page", f"Went to: {url}")
        self.wait_to_see(1)  # Wait a bit longer for page load
