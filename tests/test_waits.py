import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

BASE_URL = "https://www.demoblaze.com"

class TestWaits:

    def test_implicit_wait(self, driver):
        # implicit wait already set in conftest.py
        driver.get(BASE_URL)
        # this element loads after page renders
        element = driver.find_element(By.ID, "login2")
        assert element.is_displayed()
        print("✓ Implicit wait worked - found login button")

    def test_explicit_wait_visibility(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        # wait until login button is visible
        element = wait.until(
            EC.visibility_of_element_located((By.ID, "login2"))
        )
        assert element.is_displayed()
        print("✓ Explicit wait - element visible:", element.text)

    def test_explicit_wait_clickable(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        # wait until login button is clickable then click it
        element = wait.until(
            EC.element_to_be_clickable((By.ID, "login2"))
        )
        element.click()
        # wait until modal username field appears
        username = wait.until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        )
        assert username.is_displayed()
        print("✓ Explicit wait - modal opened successfully")

    def test_explicit_wait_presence(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        # presence = in DOM even if not visible
        element = wait.until(
            EC.presence_of_element_located((By.ID, "login2"))
        )
        assert element is not None
        print("✓ Explicit wait - element present in DOM")

    def test_fluent_wait(self, driver):
        driver.get(BASE_URL)
        # fluent wait - checks every 1 second, ignores NoSuchElementException
        wait = WebDriverWait(
            driver,
            timeout=20,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException]
        )
        element = wait.until(
            EC.visibility_of_element_located((By.ID, "login2"))
        )
        assert element.is_displayed()
        print("✓ Fluent wait worked - found element")

    def test_wait_for_alert(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        # open login modal
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        time.sleep(1)
        # type wrong credentials to trigger alert
        driver.find_element(By.ID, "loginusername").send_keys("wronguser")
        driver.find_element(By.ID, "loginpassword").send_keys("wrongpass")
        driver.find_element(
            By.XPATH, "//button[text()='Log in']"
        ).click()
        # wait for alert to appear
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("✓ Alert appeared:", alert.text)
        alert.accept()
        assert True