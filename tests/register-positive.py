import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RegisterPositive(unittest.TestCase):

    #setup browser yang dipakai / memanggil driver
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #maintest 
    def test_a_register_success(self):
        driver = self.browser
        #access url
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")
        #fill form
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("anisa")
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("blabla1232@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #respon success
        response = driver.find_element(By.XPATH, "//div[@class='result']").text
        self.assertIn("Your registration completed", response)
        self.assertIn(url, "https://demowebshop.tricentis.com/registerresult/1")
        #next page
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        response_success = driver.find_element(By.XPATH, "//a[@class='ico-logout']").text
        self.assertIn("Log out", response_success)
        #self.assertIn(url, "https://demowebshop.tricentis.com/")
        
if __name__ == '__main__':
    unittest.main()