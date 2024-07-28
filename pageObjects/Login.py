from selenium.webdriver.common.by import By


class Login:
    username = (By.XPATH, "//input[@name='username']")
    password = (By.XPATH, "//input[@name='password']")
    login = (By.CSS_SELECTOR, ".button")

    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self):
        return self.driver.find_element(*Login.username)
    def enterPwd(self):
        return self.driver.find_element(*Login.password)
    def submit(self):
        return self.driver.find_element(*Login.login)