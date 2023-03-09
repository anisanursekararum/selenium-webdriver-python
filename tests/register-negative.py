import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RegisterNegative(unittest.TestCase):

    #setup browser yang dipakai / memanggil driver
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #maintest 
    def test_a_register_empty_form(self):
        driver = self.browser
        #access url
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")
        #empty form directly click register
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response_firstname = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='FirstName']").text
        self.assertIn("First name is required.", response_firstname)
        response_lastname = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='LastName']").text
        self.assertIn("Last name is required.", response_lastname)
        response_email = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='Email']").text
        self.assertIn("Email is required.", response_email)
        response_password = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='Password']").text
        self.assertIn("Password is required.", response_password)
        response_password_confirm = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='ConfirmPassword']").text
        self.assertIn("Password is required.", response_password_confirm)
    
    def test_b_register_empty_firstname(self):
        driver = self.browser
        #access url
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")
        #firstname empty
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("blabla1232@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='FirstName']").text
        self.assertIn("First name is required.", response)

    def test_c_register_empty_lastname(self):
        driver = self.browser
        #access url
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")
        #firstname empty
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("blabla1232@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='LastName']").text
        self.assertIn("Last name is required.", response)

    def test_d_register_empty_email(self):
        driver = self.browser
        #access url
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")
        #firstname empty
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("anisa")
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='Email']").text
        self.assertIn("Email is required.", response)

    def test_e_register_empty_password(self):
        driver = self.browser
        #access url
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")
        #firstname empty
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("anisa")
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("blabla1232@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='Password']").text
        self.assertIn("Password is required.", response)

    def test_f_register_empty_confirm_password(self):
        driver = self.browser
        #access url
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")
        #firstname empty
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("anisa")
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("testing")
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("blabla1232@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='ConfirmPassword']").text
        self.assertIn("Password is required.", response)

    def test_g_register_incorrect_email(self):
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
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("heqw@.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='Email']").text
        self.assertIn("Wrong email", response)

    def test_h_register_password_less_than6(self):
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
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("heqw@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pa")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pa")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='Password']").text
        self.assertIn("The password should have at least 6 characters.", response)

    def test_i_register_password_mismatch(self):
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
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("heqw@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Pass123")
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Pa")
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        #response validation 
        response = driver.find_element(By.XPATH, "//span[@class='field-validation-error']//span[@for='ConfirmPassword']").text
        self.assertIn("The password and confirmation password do not match.", response)

    def test_j_register_email_already_registered(self):
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
        #response validation 
        response = driver.find_element(By.XPATH, "//li[normalize-space()='The specified email already exists']").text
        self.assertIn("The specified email already exists", response)

if __name__ == '__main__':
    unittest.main()