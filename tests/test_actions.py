import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.demoblaze.com"

class TestMouseActions:

    def test_hover_over_element(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        
        # hover over the login button
        element = wait.until(
            EC.visibility_of_element_located((By.ID, "login2"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        
        assert element.is_displayed()
        print("✓ Hovered over login button successfully")

    def test_click_using_actions(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        
        element = wait.until(
            EC.element_to_be_clickable((By.ID, "login2"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        time.sleep(1)
        
        # verify modal opened
        username = wait.until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        )
        assert username.is_displayed()
        print("✓ Clicked login button using ActionChains")

    def test_double_click(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        
        element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "navbar-brand"))
        )
        actions = ActionChains(driver)
        actions.double_click(element).perform()
        time.sleep(1)
        
        assert "demoblaze" in driver.current_url
        print("✓ Double clicked navbar brand")

    def test_right_click(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        
        element = wait.until(
            EC.visibility_of_element_located((By.ID, "login2"))
        )
        actions = ActionChains(driver)
        actions.context_click(element).perform()
        time.sleep(1)
        
        assert element.is_displayed()
        print("✓ Right clicked login button successfully")

    def test_scroll_to_element(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        time.sleep(2)
        
        # scroll to bottom of page using JavaScript
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        
        # scroll back to top
        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)
        
        element = wait.until(
            EC.visibility_of_element_located((By.ID, "login2"))
        )
        assert element.is_displayed()
        print("✓ Scrolled page up and down successfully")

    def test_move_to_element_and_click(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        
        # hover then click signup
        element = wait.until(
            EC.element_to_be_clickable((By.ID, "signin2"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).pause(1).click().perform()
        time.sleep(1)
        
        assert element is not None
        print("✓ Moved to element and clicked signup")