import pytest
import time
from selenium.webdriver.common.by import By

BASE_URL = "https://www.demoblaze.com"

class TestLocators:

    def test_find_by_id(self, driver):
        driver.get(BASE_URL)
        element = driver.find_element(By.ID, "login2")
        assert element.is_displayed()
        print("✓ Found by ID:", element.text)

    def test_find_by_class_name(self, driver):
        driver.get(BASE_URL)
        element = driver.find_element(By.CLASS_NAME, "navbar-brand")
        assert element.is_displayed()
        print("✓ Found by CLASS_NAME:", element.text)

    def test_find_by_tag_name(self, driver):
        driver.get(BASE_URL)
        elements = driver.find_elements(By.TAG_NAME, "h4")
        assert len(elements) > 0
        print(f"✓ Found {len(elements)} elements by TAG_NAME")

    def test_find_by_link_text(self, driver):
        driver.get(BASE_URL)
        import time
        time.sleep(3)
        element = driver.find_element(By.LINK_TEXT, "Sign up")
        assert element.is_displayed()
        print("✓ Found by LINK_TEXT:", element.text)

    def test_find_by_partial_link_text(self, driver):
        driver.get(BASE_URL)
        import time
        time.sleep(3)
        element = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")
        assert element.is_displayed()
        print("✓ Found by PARTIAL_LINK_TEXT:", element.text)

    def test_find_by_css_selector(self, driver):
        driver.get(BASE_URL)
        element = driver.find_element(By.CSS_SELECTOR, "#login2")
        assert element.is_displayed()
        print("✓ Found by CSS_SELECTOR:", element.text)

    def test_find_by_xpath(self, driver):
        driver.get(BASE_URL)
        element = driver.find_element(
            By.XPATH, "//a[contains(text(),'Home')]"
        )
        assert element.is_displayed()
        print("✓ Found by XPATH:", element.text)

    def test_find_multiple_elements(self, driver):
        driver.get(BASE_URL)
        products = driver.find_elements(
            By.CSS_SELECTOR, ".card-title a"
        )
        assert len(products) > 0
        print(f"✓ Found {len(products)} products")
        for p in products:
            print("  -", p.text)