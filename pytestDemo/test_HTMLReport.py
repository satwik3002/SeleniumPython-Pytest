import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestHollandAndBarrett:
    @pytest.fixture()
    def setup(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        # Close the browser after the test
        self.driver.quit()

    def test_homePageTitle(self, setup):
        # Navigate to the login page
        self.driver.get("https://auth.hollandandbarrett.com/u/login")
        # Assert the page title
        assert self.driver.title == "Sign in - to your account, for the best experience"

    def test_login(self, setup):
        self.driver.get("https://auth.hollandandbarrett.com/u/login")
        self.driver.find_element(By.ID, 'username').send_keys("satwikkatamaraju@gmail.com")
        self.driver.find_element(By.ID, 'password').send_keys("Y2#ssv@Xp/xP8Wt")
        self.driver.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[2]/button")
        assert self.driver.title
