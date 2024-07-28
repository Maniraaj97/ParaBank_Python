from selenium.webdriver.common.by import By


class AO:
    table_data = (By.XPATH, "//table[id='accountTable']//tr//td[2]")

    def __init__(self, driver):
        self.driver = driver

    def getTableData(self):
        return self.driver.find_elements(*AO.table_data)
