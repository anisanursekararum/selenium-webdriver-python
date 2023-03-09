import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class LoginPositive(unittest.TestCase):

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
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/login")
        response_login_page = driver.find_element(By.XPATH, "//h1[normalize-space()='Welcome, Please Sign In!']").text
        self.assertIn("Welcome, Please Sign In!", response_login_page)
        #fill form
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("blabla1232@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        #respon success
        response = driver.find_element(By.XPATH, "//a[@class='ico-logout']").text
        self.assertIn("Log out", response)
        #self.assertIn(url, "https://demowebshop.tricentis.com/")
        
if __name__ == '__main__':
    unittest.main()