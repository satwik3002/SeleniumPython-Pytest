import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.co.in")
        TitleOfBrowser = driver.title
        self.assertTrue(TitleOfBrowser == "Google")

        driver.quit()

if __name__ == "__main__":
    unittest.main()
