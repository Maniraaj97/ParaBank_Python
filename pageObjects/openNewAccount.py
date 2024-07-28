from selenium.webdriver.common.by import By


class openNewAccount:
    newAccount = (By.PARTIAL_LINK_TEXT, "Open New")
    accountType = (By.XPATH, "//select[@id='type']")
    accountFrom = (By.ID, "fromAccountId")
    openButton = (By.XPATH, "//input[@value='Open New Account']")

    def __init__(self, driver):
        self.driver = driver

    def newAccountLink(self):
        return self.driver.find_element(*openNewAccount.newAccount)

    def account(self):
        return self.driver.find_elements(*openNewAccount.accountType)

    def fromAccount(self):
        return self.driver.find_elements(*openNewAccount.accountFrom)

    def accountOpenButton(self):
        return self.driver.find_element(*openNewAccount.openButton)
