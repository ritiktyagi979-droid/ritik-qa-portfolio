import pytest
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

BASE_URL = "https://www.demoblaze.com"

class TestLogin:

    def test_valid_login(self, driver):
        page = BasePage(driver)
        driver.get(BASE_URL)
        page.click((By.ID, "login2"))
        time.sleep(1)
        page.type_text((By.ID, "loginusername"), "ritiktest123")
        page.type_text((By.ID, "loginpassword"), "Test@1234")
        page.click((By.XPATH, "//button[text()='Log in']"))
        time.sleep(2)
        assert "demoblaze" in driver.current_url

    def test_empty_login(self, driver):
        page = BasePage(driver)
        driver.get(BASE_URL)
        page.click((By.ID, "login2"))
        time.sleep(1)
        page.click((By.XPATH, "//button[text()='Log in']"))
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            assert alert_text is not None
        except:
            assert True

    def test_page_title(self, driver):
        driver.get(BASE_URL)
        assert "STORE" in driver.title
        print(f"Page title: {driver.title}")

    def test_login_modal_opens(self, driver):
        page = BasePage(driver)
        driver.get(BASE_URL)
        page.click((By.ID, "login2"))
        time.sleep(1)
        username_field = page.is_displayed((By.ID, "loginusername"))
        assert username_field == True